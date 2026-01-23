# 📚 Book Recommender System

A machine learning–powered **Book Recommendation System** that suggests books to users using **Popularity-Based Filtering** and **Collaborative Filtering** techniques.  
The system is deployed as a web application and provides personalized book recommendations based on user behavior.

🚀 **Live Demo:**  
👉 https://book-recommender-system-e9718db047f3.herokuapp.com/

---

## 📌 Project Overview

With the exponential growth of digital content, users often face difficulty in discovering books aligned with their interests.  
This project solves the problem by analyzing historical user ratings and applying recommendation algorithms to suggest relevant books.

The system supports:
- Non-personalized recommendations for new users
- Personalized recommendations using collaborative filtering
- A simple and interactive web interface

---

## 🎯 Objectives

- Build an intelligent recommendation system
- Handle cold-start and data sparsity problems
- Implement collaborative filtering using cosine similarity
- Deploy a production-ready ML application

---

## ✨ Key Features

-  **Popularity-Based Recommendation**
  - Recommends globally popular and highly rated books
  - Ideal for new users (cold-start problem)

-  **Collaborative Filtering**
  - Personalized recommendations based on similar users
  - Item-based cosine similarity

-  **Data Preprocessing**
  - Missing value handling
  - Noise and sparsity reduction
  - User and book filtering

-  **Web Application**
  - Flask-based backend
  - Deployed on Heroku

---

## Recommendation Techniques

### 1️⃣ Popularity-Based Filtering
Books are recommended based on:
- Number of ratings
- Average rating  
A minimum threshold is applied to avoid biased recommendations.

### 2️⃣ Collaborative Filtering (Item-Based)
- User–Book interaction matrix
- Cosine similarity for measuring similarity between books
- Personalized recommendations based on reading patterns

---

## Tech Stack

### Programming & Libraries
- Python
- Pandas
- NumPy
- Scikit-learn

### Web & Deployment
- Flask
- HTML / CSS
- Gunicorn
- Heroku

---

## Dataset Description

The project uses three datasets:
- **Books** – Book metadata (title, author, publisher, images)
- **Users** – User demographic information
- **Ratings** – Explicit and implicit book ratings

The dataset contains sparse interactions, making it suitable for real-world recommender system scenarios.

---

## 🚀 How to Run Locally

1️⃣ Clone the repository:
```bash
git clone https://github.com/your-username/book-recommender-system.git
```

2️⃣ Navigate to the project directory:
```bash
cd book-recommender-system
```

3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

4️⃣ Run the Flask application:
```bash
python app.py
```

5️⃣ Open in browser:
```bash
http://127.0.0.1:5000/
```
