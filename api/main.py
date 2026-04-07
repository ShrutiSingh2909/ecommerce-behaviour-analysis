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

@app.get("/top-states")
def top_states():
    data = df.groupby("customer_state")["total_spend"].sum().nlargest(5)
    return data.to_dict()

@app.get("/payment-types")
def payment_types():
    return df["payment_type"].value_counts().to_dict()