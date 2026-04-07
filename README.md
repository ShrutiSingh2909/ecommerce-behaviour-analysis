# 🛒 E-Commerce Behaviour Analysis

A complete end-to-end Data Analytics project analyzing 
customer behaviour, sales trends, and purchase patterns.

## 🔧 Tech Stack
- **Python** — Pandas, NumPy, Scikit-learn, Plotly
- **PostgreSQL** — Supabase (cloud database)
- **Power BI** — Interactive dashboard
- **FastAPI** — REST API for predictions
- **Streamlit** — Interactive web app

## 📁 Project Structure
- `src/` — Preprocessing, EDA, ML scripts
- `api/` — FastAPI backend
- `app/` — Streamlit frontend
- `dashboard/` — Power BI file
- `models/` — Saved ML models
- `data/` — Raw and processed data

## 🚀 How to Run

### 1. Clone the repo
git clone https://github.com/yourusername/ecommerce-behaviour-analysis.git
cd ecommerce-behaviour-analysis

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run FastAPI
uvicorn api.main:app --reload

### 4. Run Streamlit
streamlit run app/streamlit_app.py

## 📊 Dashboard
Built using Power BI with KPIs, revenue trends,
customer segments and filters.

## 🤖 ML Models
- K-Means Clustering — Customer Segmentation
- Random Forest — High Value Customer Prediction

## 📌 Dataset
Brazilian E-Commerce Dataset — Kaggle
