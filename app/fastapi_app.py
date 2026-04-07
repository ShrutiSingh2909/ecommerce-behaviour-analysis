from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("C:/Users/shruti/Documents/projects/ecommerce-behaviour-analysis/data/processed/cleaned_data.csv")

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.get("/total-revenue")
def total_revenue():
    revenue = df["total_spend"].sum()
    return {"total_revenue": float(revenue)}