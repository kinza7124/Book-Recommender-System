import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Page config
st.set_page_config(
    page_title="Book Recommender",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .book-card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .recommendation-card {
        background: rgba(56, 189, 248, 0.1);
        border-left: 4px solid #38bdf8;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div style='text-align: center; margin-bottom: 2rem;'>
    <h1>📚 Book Recommender System</h1>
    <p style='color: #9ca3af;'>Discover your next favorite book</p>
</div>
""", unsafe_allow_html=True)

# Load data
@st.cache_resource
def load_data():
    try:
        books_df = pd.read_csv('Books.csv', low_memory=False)
        
        with open('popular.pkl', 'rb') as f:
            popular_df = pickle.load(f)
        
        with open('pt.pkl', 'rb') as f:
            pt = pickle.load(f)
        
        with open('similarity_scores.pkl', 'rb') as f:
            similarity_scores = pickle.load(f)
        
        with open('books.pkl', 'rb') as f:
            books = pickle.load(f)
        
        return books_df, popular_df, pt, similarity_scores, books
    except FileNotFoundError as e:
        st.error(f"Error loading model files: {e}")
        st.info("Make sure all .pkl and .csv files are uploaded to the Space")
        return None, None, None, None, None

books_df, popular_df, pt, similarity_scores, books = load_data()

if books_df is None:
    st.stop()

# Tabs
tab1, tab2 = st.tabs(["📊 Popular Books", "🔍 Get Recommendations"])

# Tab 1: Popular Books
with tab1:
    st.subheader("Most Popular Books This Month")
    
    # Display popular books
    cols = st.columns(5)
    for idx, (_, row) in enumerate(popular_df.head(15).iterrows()):
        with cols[idx % 5]:
            st.markdown('<div class="book-card">', unsafe_allow_html=True)
            try:
                st.image(row['Image-URL-M'], use_column_width=True)
            except:
                st.image("https://via.placeholder.com/150x200?text=No+Image", use_column_width=True)
            
            st.markdown(f"**{row['Book-Title'][:25]}...**" if len(row['Book-Title']) > 25 else f"**{row['Book-Title']}**")
            st.markdown(f"<small>👤 {row['Book-Author'][:20]}...</small>" if len(row['Book-Author']) > 20 else f"<small>👤 {row['Book-Author']}</small>", unsafe_allow_html=True)
            st.markdown(f"<small>⭐ {row.get('avg_rating', 0):.2f}</small>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Tab 2: Recommendations
with tab2:
    st.subheader("Get Personalized Recommendations")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        book_title = st.selectbox(
            "Select a book you like:",
            sorted(pt.index.tolist()),
            help="Choose a book to find similar recommendations"
        )
    
    with col2:
        recommend_btn = st.button("🎯 Get Recommendations", use_container_width=True)
    
    if recommend_btn:
        try:
            # Find book index
            index = np.where(pt.index == book_title)[0]
            
            if len(index) == 0:
                st.error("❌ Book not found!")
            else:
                # Get similar books
                similar_items = sorted(
                    list(enumerate(similarity_scores[index[0]])),
                    key=lambda x: x[1],
                    reverse=True
                )[1:6]
                
                st.success("✅ Here are books similar to what you selected:")
                st.markdown("---")
                
                for rank, (book_idx, score) in enumerate(similar_items, 1):
                    rec_book = pt.index[book_idx]
                    book_data = books.get(rec_book, {})
                    
                    col1, col2, col3 = st.columns([1, 3, 1])
                    
                    with col1:
                        try:
                            st.image(book_data.get('Image-URL-M', 'https://via.placeholder.com/100x150'), width=80)
                        except:
                            st.image("https://via.placeholder.com/100x150", width=80)
                    
                    with col2:
                        st.markdown(f"**{rank}. {rec_book}**")
                        if 'Book-Author' in book_data:
                            st.markdown(f"👤 Author: {book_data['Book-Author']}")
                        st.markdown(f"📊 Match Score: **{score:.2%}**")
                    
                    with col3:
                        st.markdown(f"<div style='text-align: center; font-size: 2rem; color: #38bdf8;'>{score:.0%}</div>", unsafe_allow_html=True)
                    
                    st.markdown("---")
        
        except Exception as e:
            st.error(f"❌ Error generating recommendations: {str(e)}")
            st.info("Try selecting a different book or check the model files")

# Sidebar
with st.sidebar:
    st.markdown("### 📊 Statistics")
    st.metric("Total Books", len(books_df))
    st.metric("Books in Recommender", len(pt.index))
    
    st.markdown("### ℹ️ About")
    st.markdown("""
    This app uses **collaborative filtering** to recommend books based on user ratings and similarities.
    
    - 📚 Dataset: 270K+ books
    - ⭐ Ratings from 1M+ users
    - 🤖 ML Algorithm: Cosine Similarity
    """)
    
    st.markdown("### 🔗 Links")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🐙 GitHub", "https://github.com/kinza7124/Book-Recommender-System")
    with col2:
        st.link_button("🤗 Hugging Face", "https://huggingface.co/spaces")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #9ca3af; font-size: 0.9rem;'>
    Made with ❤️ using Streamlit | 
    <a href='https://github.com/kinza7124/Book-Recommender-System' target='_blank'>View on GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
