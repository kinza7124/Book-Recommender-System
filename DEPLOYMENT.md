# Book Recommender System - Deployment Guide

## Local Deployment

### Prerequisites
- Docker installed ([Download](https://docs.docker.com/get-docker/))
- Docker Compose installed (usually included with Docker Desktop)

### Option 1: Docker Compose (Easiest)

```bash
# Clone the repository
git clone https://github.com/kinza7124/Book-Recommender-System.git
cd Book-Recommender-System

# Run with Docker Compose
docker-compose up

# Application will be available at http://localhost:5000
```

### Option 2: Docker Build & Run

```bash
# Build the image
docker build -t book-recommender .

# Run the container
docker run -p 5000:5000 book-recommender

# Application will be available at http://localhost:5000
```

---

## Cloud Deployment

### Heroku

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create a new app
heroku create your-app-name

# Add Procfile (already included)
# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Railway.app

1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Connect your GitHub account
5. Select `Book-Recommender-System` repository
6. Railway will auto-detect Dockerfile and deploy
7. Your app will be available at the provided Railway URL

### AWS (ECS/Fargate)

```bash
# Create ECR repository
aws ecr create-repository --repository-name book-recommender

# Build and push image
docker build -t book-recommender .
docker tag book-recommender:latest <your-aws-account>.dkr.ecr.<region>.amazonaws.com/book-recommender:latest
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <your-aws-account>.dkr.ecr.<region>.amazonaws.com
docker push <your-aws-account>.dkr.ecr.<region>.amazonaws.com/book-recommender:latest

# Create ECS task definition and service in AWS Console
# Or use CLI: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service.html
```

### DigitalOcean

1. Go to [digitalocean.com](https://digitalocean.com)
2. Create App Platform App
3. Connect your GitHub repository
4. DigitalOcean will detect Dockerfile automatically
5. Configure environment and deploy

### Google Cloud Run

```bash
# Authenticate with Google Cloud
gcloud auth login

# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/<your-project>/book-recommender

# Deploy to Cloud Run
gcloud run deploy book-recommender \
  --image gcr.io/<your-project>/book-recommender \
  --platform managed \
  --region us-central1 \
  --port 5000 \
  --memory 512Mi
```

---

## Environment Variables

Create a `.env` file (optional):

```
FLASK_ENV=production
FLASK_DEBUG=0
```

## Troubleshooting

### Port already in use
```bash
# Change port mapping
docker run -p 8080:5000 book-recommender
# Then access at http://localhost:8080
```

### Container won't start
```bash
# Check logs
docker logs <container-id>

# Rebuild without cache
docker build --no-cache -t book-recommender .
```

### Large file issues
The Books.csv is ~70MB. For cloud deployments, consider:
- Using Git LFS
- Downloading data at runtime
- Using cloud storage (S3, GCS)

---

## Production Recommendations

1. **Use managed services** for easier maintenance
2. **Set up monitoring** and logging
3. **Configure auto-scaling** for high traffic
4. **Use a reverse proxy** (nginx) for multiple instances
5. **Enable HTTPS/SSL** certificates
6. **Set resource limits** on containers (CPU, Memory)

## Quick Deploy Commands

**Railway (30 seconds):**
```bash
git push
# Automatic deployment on push
```

**Local:**
```bash
docker-compose up
```

**AWS:**
```bash
docker build -t book-recommender . && docker push <registry>/book-recommender
```

---

For questions or issues, check the [GitHub repository](https://github.com/kinza7124/Book-Recommender-System).
