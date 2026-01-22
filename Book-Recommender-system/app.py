import os
from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load popular books once at startup for fast responses
with open(os.path.join(BASE_DIR, 'popular.pkl'), 'rb') as f:
    popular_df = pickle.load(f)

# Load book metadata for rendering recommendation cards (prefer high-res images)
books_df = pd.read_csv(os.path.join(BASE_DIR, 'Books.csv'), low_memory=False)
book_meta = (
    books_df[['Book-Title', 'Book-Author', 'Image-URL-M', 'Image-URL-L']]
    .drop_duplicates(subset=['Book-Title'])
    .set_index('Book-Title')
    .to_dict(orient='index')
)


def proxied_image(url: str, title: str = '', author: str = '') -> str:
    """Convert HTTP Amazon image URLs to HTTPS and provide fallback for missing images."""
    if not url or url.strip() == '':
        # Generate a professional placeholder with book info
        title_encoded = title.replace(' ', '+')[:30]
        author_encoded = author.replace(' ', '+')[:20]
        return f'https://via.placeholder.com/200x300?text={title_encoded}%0A{author_encoded}'
    # If already https, keep it
    if url.startswith('https://'):
        return url
    # Convert http to https for Amazon URLs
    if url.startswith('http://'):
        return url.replace('http://', 'https://', 1)
    return url

# Hydrate popular list with high-res images when available
popular_books = []
for row in popular_df.head(50).fillna('').to_dict(orient='records'):
    meta = book_meta.get(row['Book-Title'], {})
    img = meta.get('Image-URL-L') or meta.get('Image-URL-M') or row.get('Image-URL-M')
    popular_books.append({
        'Book-Title': row['Book-Title'],
        'Book-Author': row['Book-Author'],
        'Image-URL': proxied_image(img, row['Book-Title'], row['Book-Author']),
    })

# Load pivot table and similarity scores for content-based recommendations
pt_path = os.path.abspath(os.path.join(BASE_DIR, '..', 'pt.pkl'))
sim_path = os.path.abspath(os.path.join(BASE_DIR, '..', 'similarity_scores.pkl'))
pt = pickle.load(open(pt_path, 'rb'))
similarity_scores = pickle.load(open(sim_path, 'rb'))

# Fast lookup for title matching (case-insensitive)
title_lookup = {title.lower(): title for title in pt.index}


def get_recommendations(book_name):
    key = book_name.lower()
    if key not in title_lookup:
        return []

    title = title_lookup[key]
    index = pt.index.get_loc(title)
    sim_scores = list(enumerate(similarity_scores[index]))
    similar_items = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    results = []
    for i, score in similar_items:
        sim_title = pt.index[i]
        meta = book_meta.get(sim_title, {})
        img = meta.get('Image-URL-L') or meta.get('Image-URL-M')
        author = meta.get('Book-Author', 'Unknown author')
        results.append({
            'Book-Title': sim_title,
            'Book-Author': author,
            'Image-URL': proxied_image(img, sim_title, author),
            'score': score,
        })
    return results


@app.route('/')
def home():
    return render_template('index.html', books=popular_books)


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    recommendations = []
    query = ''

    if request.method == 'POST':
        query = request.form.get('book_name', '').strip()
        if query:
            recommendations = get_recommendations(query)

    return render_template('recommend.html', recommendations=recommendations, query=query)


if __name__ == '__main__':
    app.run(debug=True)
