import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("C:/Users/shruti/Documents/projects/ecommerce-behaviour-analysis/data/processed/cleaned_data.csv")

# 1. Monthly Revenue Trend
monthly = df.groupby(
    ["year_of_purchase", "month_of_purchase"]
)["total_spend"].sum().reset_index()

monthly = monthly.sort_values("month_of_purchase")

plt.figure(figsize=(14, 5))

sns.lineplot(
    data=monthly,
    x="month_of_purchase",
    y="total_spend",
    hue="year_of_purchase",
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("data/processed/monthly_revenue.png")
plt.show()

# 2. Top 10 Product Categories
top_cats = df.groupby("product_category_name")["total_spend"].sum().nlargest(10)
plt.figure(figsize=(12, 5))
top_cats.plot(kind="bar", color="steelblue")
plt.title("Top 10 Product Categories by Revenue")
plt.savefig("data/processed/top_categories.png")
plt.show()

# 3. Payment Type Distribution
plt.figure(figsize=(8, 4))
df["payment_type"].value_counts().plot(kind="bar", color="coral")
plt.title("Payment Method Distribution")
plt.savefig("data/processed/payment_distribution.png")
plt.show()

# 4. Revenue by State
state_rev = df.groupby("customer_state")["total_spend"].sum().nlargest(10)
plt.figure(figsize=(12, 5))
state_rev.plot(kind="bar", color="green")
plt.title("Top 10 States by Revenue")
plt.savefig("data/processed/state_revenue.png")
plt.show()

# 5. Order Status Distribution
plt.figure(figsize=(8, 4))
df["order_status"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Order Status Distribution")
plt.savefig("data/processed/order_status.png")
plt.show()

print("EDA done!")