---
title: Book Recommender System
emoji: 📚
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
---

# 📚 Book Recommender System

A machine learning-powered book recommendation system using collaborative filtering. Discover your next favorite book based on your reading preferences!

## Features

✨ **Popular Books Discovery**
- Browse trending and highly-rated books
- Beautiful card-based layout
- Book cover images and ratings

🔍 **Smart Recommendations**
- Search for any book
- Get personalized recommendations based on similarity
- Match score percentages
- Author and rating information

🚀 **Performance**
- Fast recommendations using precomputed similarity scores
- Optimized for Hugging Face Spaces
- Handles 270K+ books

## How It Works

The system uses **content-based filtering** with cosine similarity to recommend books:

1. **User selects** a book they like
2. **Algorithm computes** similarity scores to other books
3. **Top 5 most similar** books are recommended
4. **Results display** with match percentages

## Dataset

- **Total Books**: 270,000+
- **User Ratings**: 1 million+
- **Features**: Title, Author, ISBN, Publication Year, Publisher, Image URLs, Ratings

## Technology Stack

- **Backend**: Flask (Python web framework)
- **ML**: Scikit-learn (similarity computation)
- **Data Processing**: Pandas, NumPy
- **Deployment**: Docker, Hugging Face Spaces

## Local Usage

### Clone the Repository

```bash
git clone https://huggingface.co/spaces/kkinza/book_recommender_system
cd book_recommender_system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
# For production (Hugging Face)
python hf_app.py

# For local development
python app.py
```

Then open your browser:
- **Development**: http://localhost:5000
- **Production**: http://localhost:7860

## File Structure

```
book_recommender_system/
├── hf_app.py                      # Flask app for Hugging Face
├── app.py                         # Flask app for local development
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Local deployment
├── Dockerfile.hf                  # Hugging Face deployment
├── Books.csv                      # Book dataset
├── popular.pkl                    # Popular books model
├── pt.pkl                         # Pivot table (user-book matrix)
├── similarity_scores.pkl          # Precomputed similarity matrix
├── books.pkl                      # Book metadata cache
├── templates/
│   ├── index.html                # Home page
│   └── recommend.html            # Recommendations page
└── README.md                      # This file
```

## Requirements

- Python 3.11+
- Flask 2.0+
- Pandas, NumPy, Scikit-learn
- ~500MB disk space (for models)

## Performance

⚡ **Recommendation Time**: < 100ms
📊 **Memory Usage**: ~2GB (with all models)
🎯 **Accuracy**: Based on user rating patterns

## Troubleshooting

### Models not found
Ensure all `.pkl` and `.csv` files are in the root directory:
```bash
ls *.pkl *.csv
```

### Port already in use
Change the port in app:
```python
app.run(host='0.0.0.0', port=8000)
```

### Large file issues
The `Books.csv` is ~70MB. If upload fails:
1. Use the web interface to upload files
2. Or use Git LFS: `git lfs install && git lfs track "*.csv"`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with popular books |
| `/recommend` | POST | Get recommendations for a book |

### Example Request

```bash
curl -X POST http://localhost:7860/recommend \
  -d "book_name=Harry Potter and the Sorcerer's Stone"
```

## Deployment

### Hugging Face Spaces (This Setup)

The Docker configuration is optimized for Hugging Face:
- Listens on port 7860
- Non-root user for security
- Health checks enabled
- Efficient image size (~800MB)

### Docker (Local)

```bash
docker build -f Dockerfile.hf -t book-recommender .
docker run -p 7860:7860 book-recommender
```

### Traditional Server

```bash
python hf_app.py
```

## Contributing

Found a bug? Have a suggestion?
- [Open an issue](https://github.com/kinza7124/Book-Recommender-System/issues)
- [Submit a PR](https://github.com/kinza7124/Book-Recommender-System/pulls)

## License

MIT License - feel free to use this in your projects!

## Links

🔗 **[GitHub Repository](https://github.com/kinza7124/Book-Recommender-System)**
🐙 **[Author's GitHub](https://github.com/kinza7124)**
📚 **[Hugging Face Hub](https://huggingface.co/kkinza)**

---

**Made with ❤️ using Flask and Machine Learning**

Last updated: January 2026
