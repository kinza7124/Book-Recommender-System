# Hugging Face Spaces Deployment Guide

## Quick Start (2 minutes)

### Option 1: Using Streamlit (Recommended)

1. **Create a Hugging Face account** → https://huggingface.co
2. **Create a new Space**:
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Choose name: `book-recommender`
   - Select **Streamlit** as SDK
   - Click "Create Space"

3. **Upload files**:
   - Go to "Files" tab
   - Upload `streamlit_app.py` (see code below)
   - Upload model files: `popular.pkl`, `pt.pkl`, `similarity_scores.pkl`, `books.pkl`
   - Upload `Books.csv`

4. **Done!** → Your app will deploy automatically ✅

---

## Step-by-Step Setup

### Step 1: Create Hugging Face Account
- Go to https://huggingface.co/signup
- Verify email
- Create API token at https://huggingface.co/settings/tokens

### Step 2: Create New Space

```bash
# Option A: Web Interface (Easiest)
# 1. Visit https://huggingface.co/spaces
# 2. Click "Create new Space"
# 3. Choose Streamlit
# 4. Name: book-recommender
# 5. Click Create

# Option B: CLI
pip install huggingface-hub
huggingface-cli login
huggingface-cli repo create book-recommender --type space --space-sdk streamlit
```

### Step 3: Push Code to Space

```bash
# Clone your space locally
git clone https://huggingface.co/spaces/your-username/book-recommender
cd book-recommender

# Copy app files
cp ../Book-Recommender-System/streamlit_app.py .
cp ../Book-Recommender-System/*.pkl .
cp ../Book-Recommender-System/Books.csv .

# Create requirements.txt
cat > requirements.txt << EOF
streamlit
pandas
numpy
scikit-learn
EOF

# Push to Hugging Face
git add .
git commit -m "Deploy Book Recommender"
git push
```

---

## Streamlit App Code

Create `streamlit_app.py`:

```python
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
    .header {
        text-align: center;
        color: #38bdf8;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="header">📚 Book Recommender System</div>', unsafe_allow_html=True)

# Load data
@st.cache_resource
def load_data():
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

books_df, popular_df, pt, similarity_scores, books = load_data()

# Tabs
tab1, tab2 = st.tabs(["📊 Popular Books", "🔍 Get Recommendations"])

# Tab 1: Popular Books
with tab1:
    st.subheader("Most Popular Books")
    
    cols = st.columns(5)
    for idx, row in popular_df.head(15).iterrows():
        with cols[idx % 5]:
            st.write(f"**{row['Book-Title']}**")
            st.write(f"👤 {row['Book-Author']}")
            st.write(f"⭐ {row['avg_rating']:.2f}")
            st.image(row['Image-URL-M'], use_column_width=True)

# Tab 2: Recommendations
with tab2:
    st.subheader("Get Personalized Recommendations")
    
    # Book selection
    book_title = st.selectbox(
        "Select a book:",
        books_df['Book-Title'].unique()
    )
    
    if st.button("Get Recommendations", key="recommend"):
        try:
            # Find book index
            index = np.where(pt.index == book_title)[0]
            
            if len(index) == 0:
                st.error("Book not found!")
            else:
                similar_items = sorted(
                    list(enumerate(similarity_scores[index[0]])),
                    key=lambda x: x[1],
                    reverse=True
                )[1:6]
                
                st.success("🎯 Recommended Books:")
                
                cols = st.columns(5)
                for idx, (book_idx, score) in enumerate(similar_items):
                    with cols[idx % 5]:
                        book_data = books.get(pt.index[book_idx], {})
                        st.write(f"**{pt.index[book_idx]}**")
                        if 'Book-Author' in book_data:
                            st.write(f"👤 {book_data['Book-Author']}")
                        if 'Image-URL-M' in book_data:
                            st.image(book_data['Image-URL-M'], use_column_width=True)
                        st.write(f"Match: {score:.2%}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
    📖 Book Recommender System | 
    <a href='https://github.com/kinza7124/Book-Recommender-System'>GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
```

---

## File Structure for Hugging Face Space

```
book-recommender/
├── streamlit_app.py          # Main Streamlit app
├── requirements.txt          # Python dependencies
├── Books.csv                 # Book data
├── popular.pkl              # Popular books model
├── pt.pkl                   # Pivot table
├── similarity_scores.pkl    # Similarity matrix
├── books.pkl                # Books metadata
└── README.md                # Space description
```

---

## Method 2: Use Docker in Spaces

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "streamlit_app.py"]
```

Then set SDK to "Docker" when creating the Space.

---

## Method 3: Keep Flask + Gradio

Install both and create `app.py`:

```python
import gradio as gr
import pickle
import numpy as np

# Load models
with open('pt.pkl', 'rb') as f:
    pt = pickle.load(f)

with open('similarity_scores.pkl', 'rb') as f:
    similarity_scores = pickle.load(f)

def recommend_books(book_title):
    try:
        index = np.where(pt.index == book_title)[0][0]
        similar = sorted(enumerate(similarity_scores[index]), key=lambda x: x[1], reverse=True)[1:6]
        recommendations = [pt.index[i[0]] for i in similar]
        return "\n".join(recommendations)
    except:
        return "Book not found"

interface = gr.Interface(
    fn=recommend_books,
    inputs=gr.Dropdown(pt.index.tolist()),
    outputs="text",
    title="Book Recommender"
)

interface.launch(server_name="0.0.0.0", server_port=7860)
```

---

## Deploy Steps Summary

### Fastest Way (Streamlit):

1. Go to https://huggingface.co/spaces
2. Click "Create new Space" → Choose "Streamlit"
3. Upload `streamlit_app.py` + model files
4. Done! ✅ (Auto-deploys on file upload)

### With Git:

```bash
git clone https://huggingface.co/spaces/your-username/book-recommender
cd book-recommender
cp ~/Book-Recommender-System/{streamlit_app.py,*.pkl,Books.csv} .
echo "streamlit\npandas\nnumpy\nscikit-learn" > requirements.txt
git add .
git commit -m "Deploy app"
git push
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Files too large | Use `git-lfs` or upload via web UI |
| App crashes | Check Space logs in Settings |
| Dependencies missing | Add to `requirements.txt` |
| Out of memory | Use `@st.cache_resource` to cache data |

---

## Live Demo Features

✅ Popular books display
✅ Book recommendation search
✅ Book covers and ratings
✅ Real-time processing
✅ Public shareable link
✅ Free hosting

Your Space URL: `https://huggingface.co/spaces/your-username/book-recommender`

