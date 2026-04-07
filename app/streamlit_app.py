import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px

model = joblib.load("C:/Users/shruti/Documents/projects/ecommerce-behaviour-analysis/models/rf_model.pkl")
df = pd.read_csv("C:/Users/shruti/Documents/projects/ecommerce-behaviour-analysis/data/processed/segmented_data.csv")

st.title("🛒 E-Commerce Behaviour Analysis")

# --- Sidebar Prediction ---
st.sidebar.header("🔍 Predict Customer Type")
tenure = st.sidebar.slider("Tenure (days)", 0, 700, 100)
installments = st.sidebar.slider("Payment Installments", 1, 24, 3)
price = st.sidebar.number_input("Product Price (R$)", 10.0, 5000.0, 200.0)
freight = st.sidebar.number_input("Freight Value (R$)", 0.0, 500.0, 20.0)

if st.sidebar.button("Predict"):
    features = np.array([[tenure, installments, price, freight]])
    pred = model.predict(features)[0]
    result = "🌟 High Value Customer" if pred == 1 else "👤 Regular Customer"
    st.sidebar.success(result)

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"R$ {df['total_spend'].sum():,.0f}")
col2.metric("Total Orders", f"{df['order_id'].nunique():,}")
col3.metric("Avg Order Value", f"R$ {df['total_spend'].mean():,.2f}")

# --- Charts ---
st.header("📈 Monthly Revenue Trend")
monthly = df.groupby(["year_of_purchase", "month_of_purchase"])["total_spend"].sum().reset_index()
fig1 = px.line(monthly, x="month_of_purchase", y="total_spend", color="year_of_purchase")
st.plotly_chart(fig1)

st.header("🏆 Top Product Categories")
top_cats = df.groupby("product_category_name")["total_spend"].sum().nlargest(10).reset_index()
fig2 = px.bar(top_cats, x="product_category_name", y="total_spend", color="total_spend")
st.plotly_chart(fig2)

st.header("🧩 Customer Segments")
fig3 = px.scatter(df, x="tenure", y="total_spend", color="segment",
                  title="Customer Segments by Tenure & Spend")
st.plotly_chart(fig3)

st.header("💳 Payment Methods")
fig4 = px.pie(df, names="payment_type", title="Payment Type Distribution")
st.plotly_chart(fig4)