# 🚀 Deploy to Hugging Face Spaces (Docker)

## Step 1: Create Your Space

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in:
   - **Space name**: `book_recommender_system`
   - **License**: MIT
   - **SDK**: Select **Docker** (not Streamlit)
4. Click **"Create Space"**

---

## Step 2: Clone Your Space Repository

Open terminal and run:

```bash
git clone https://huggingface.co/spaces/your-username/book_recommender_system
cd book_recommender_system
```

When prompted for password, use a **Personal Access Token**:
- Generate at: https://huggingface.co/settings/tokens
- Click "New token" → Type: Read/Write
- Copy token and paste when prompted

---

## Step 3: Add Your Project Files

Copy all files from the original repository:

```bash
# Copy Python files
cp /path/to/Book-Recommender-System/hf_app.py .
cp /path/to/Book-Recommender-System/Dockerfile.hf Dockerfile

# Copy model files
cp /path/to/Book-Recommender-System/popular.pkl .
cp /path/to/Book-Recommender-System/pt.pkl .
cp /path/to/Book-Recommender-System/similarity_scores.pkl .
cp /path/to/Book-Recommender-System/books.pkl .

# Copy data
cp /path/to/Book-Recommender-System/Books.csv .

# Copy templates
cp -r /path/to/Book-Recommender-System/templates .
```

---

## Step 4: Create requirements.txt

```bash
cat > requirements.txt << 'EOF'
Flask==3.0.0
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
gunicorn==21.2.0
EOF
```

---

## Step 5: Create README.md

Copy the content from [README_HF.md](README_HF.md) to a new `README.md`:

```bash
cp README_HF.md README.md
```

---

## Step 6: Create Dockerfile

The Dockerfile should look like:

```dockerfile
FROM python:3.11-slim

RUN useradd -m -u 1000 user
USER user

ENV PATH="/home/user/.local/bin:$PATH"
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --chown=user requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user . /app

EXPOSE 7860

HEALTHCHECK CMD python -c "import requests; requests.get('http://localhost:7860')" || exit 1

CMD ["python", "hf_app.py"]
```

---

## Step 7: Commit and Push

```bash
git add .
git commit -m "Deploy Book Recommender System"
git push
```

---

## Step 8: Wait for Deployment

1. Go to your Space page
2. Click **"Logs"** tab to monitor
3. Wait for "Building Docker image..."
4. Once complete, your app is LIVE! 🎉

Your Space URL: `https://huggingface.co/spaces/your-username/book_recommender_system`

---

## File Size Warning

**Books.csv is ~70MB**, which may take time to upload. Options:

### Option A: Upload via Web UI (Easiest)
1. Go to Files tab in your Space
2. Click "Upload file"
3. Select each file individually
4. Commit changes

### Option B: Use Git LFS
```bash
git lfs install
git lfs track "*.csv"
git add .gitattributes
git commit -m "Setup LFS"
git push
```

### Option C: Split the File
Split `Books.csv` into smaller chunks (not recommended)

---

## Troubleshooting

### Build Fails: "Memory Error"
- Hugging Face Spaces have limited RAM
- Reduce model loading in `hf_app.py`
- Or upgrade to a better hardware option

### App Crashes: "Port already in use"
- The port 7860 is reserved for Hugging Face
- It's hardcoded in `hf_app.py`

### Models Not Found
Ensure these files are in root:
```
books.pkl
similarity_scores.pkl
popular.pkl
pt.pkl
Books.csv
```

### Slow Load Times
First request is slow due to model loading. This is normal.

---

## Environment Variables (Optional)

Add to Space settings if needed:

```
FLASK_ENV=production
PYTHONUNBUFFERED=1
```

---

## Monitor Your Space

After deployment:

1. **Check Logs**: Click "Logs" in top menu
2. **View Stats**: See CPU/Memory usage
3. **Check Uptime**: Space should always be running
4. **Get Shareable Link**: Share with https://huggingface.co/spaces/your-username/book_recommender_system

---

## Next Steps

✅ App is deployed!

Now you can:
- Share the link with friends
- Embed it on your website
- Add to your portfolio
- Integrate with other apps

---

## Quick Reference

| Item | Value |
|------|-------|
| **Port** | 7860 |
| **Framework** | Flask + Docker |
| **Max Models** | 5 (.pkl files) |
| **RAM Available** | ~2GB |
| **CPU** | Shared |
| **Disk** | Limited (~100GB) |

---

Need help? Check [GitHub Issues](https://github.com/kinza7124/Book-Recommender-System/issues)
