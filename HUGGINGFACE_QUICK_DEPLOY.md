# 📚 Hugging Face Spaces Deployment - QUICK START

## Your Space Created: `kkinza/book_recommender_system`

---

## 🎯 3-Step Deployment

### **STEP 1**: Clone Your Space
```bash
git clone https://huggingface.co/spaces/kkinza/book_recommender_system
cd book_recommender_system
```
Use your **Hugging Face token** as password.

---

### **STEP 2**: Copy Files

**Option A - Automated Script:**
```bash
# Download our deployment script (coming soon)
# For now, manually copy:
```

**Option B - Manual Copy:**
```bash
# From your Book-Recommender-System repo:

# Copy app
cp ../Book-Recommender-System/hf_app.py .

# Copy models
cp ../Book-Recommender-System/popular.pkl .
cp ../Book-Recommender-System/pt.pkl .
cp ../Book-Recommender-System/similarity_scores.pkl .
cp ../Book-Recommender-System/books.pkl .

# Copy data
cp ../Book-Recommender-System/Books.csv .

# Copy templates
cp -r ../Book-Recommender-System/templates .
```

---

### **STEP 3**: Commit & Push
```bash
git add .
git commit -m "Deploy Flask Book Recommender"
git push
```

**Wait 2-5 minutes...** ⏳ Hugging Face builds Docker image

**Your app is LIVE!** 🚀

---

## 📋 Files Needed in Your Space

```
✅ hf_app.py              (Flask app)
✅ Dockerfile             (already in repo)
✅ requirements.txt       (already in repo)
✅ Books.csv              (70 MB - large file)
✅ popular.pkl            (model)
✅ pt.pkl                 (model)
✅ similarity_scores.pkl  (model)
✅ books.pkl              (metadata)
✅ templates/             (folder with HTML)
✅ README.md              (description)
```

---

## ⚠️ Important Notes

### Port 7860
- ✅ Already configured in `hf_app.py`
- ✅ Hugging Face Spaces requires this
- No changes needed!

### Large File Upload
**Books.csv is 70MB** - two options:

**Option 1: Upload via Web UI (Easy)**
1. Go to Files tab in your Space
2. Click "Upload file"
3. Select Books.csv
4. Commit

**Option 2: Use Git LFS**
```bash
git lfs install
git lfs track "*.csv"
git add .gitattributes
git commit -m "Add LFS tracking"
git push
```

---

## 🔍 Monitoring Your Space

After pushing, check:
1. Click **"Logs"** → See build progress
2. Wait for ✅ **"Build successful"**
3. App automatically restarts
4. **Refresh page** → Your app is live!

**URL**: https://huggingface.co/spaces/kkinza/book_recommender_system

---

## 🎨 Customize Your Space (Optional)

Edit README.md to change:
- Title & emoji
- Description
- Links

**Front matter in README.md:**
```yaml
---
title: Book Recommender System
emoji: 📚
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
---
```

---

## ✨ What You Get

✅ Free hosting (Community tier)
✅ Public shareable link
✅ Auto-restart on crash
✅ Git-based deployments
✅ Docker support
✅ Custom domain (optional)

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Build fails | Check logs, ensure all files present |
| App won't start | Verify `hf_app.py` uses port 7860 |
| Can't upload Books.csv | Use Git LFS or upload via web UI |
| App is slow | First load is slow (models loading). Normal! |
| 404 on paths | Check `templates/` folder exists |

---

## 📖 Reference

**Files in this repo:**
- `hf_app.py` - Flask app for Hugging Face
- `Dockerfile.hf` - Docker config (renamed to `Dockerfile` in Space)
- `HUGGINGFACE_DOCKER_DEPLOY.md` - Detailed guide
- `README_HF.md` - Full documentation

**Original files:**
- `app.py` - Local development
- `Book-Recommender-System/` - Flask templates & data

---

## 🚀 Ready?

```bash
git clone https://huggingface.co/spaces/kkinza/book_recommender_system
cd book_recommender_system
# Copy files (see STEP 2 above)
git add .
git commit -m "Deploy"
git push
```

Your app deploys automatically! ✨

---

**Questions?** See [HUGGINGFACE_DOCKER_DEPLOY.md](HUGGINGFACE_DOCKER_DEPLOY.md)
