import pandas as pd

def preprocess():
    df = pd.read_csv("C:/Users/shruti/Documents/projects/ecommerce-behaviour-analysis/data/raw/Brazilian E-Commerce Public Dataset by Olist.csv")

    # Convert date columns
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"], dayfirst=True)

    # Feature Engineering
    df["total_spend"] = df["payment_value"]
    df["tenure"] = (df["order_purchase_timestamp"].max() - 
                    df["order_purchase_timestamp"]).dt.days

    # Keep useful columns only
    df = df[[
        "order_id", "customer_unique_id", "customer_city", "customer_state",
        "product_category_name", "payment_type", "payment_installments",
        "price", "freight_value", "total_spend", "tenure",
        "year_of_purchase", "month_of_purchase", "day_of_purchase",
        "order_status", "seller_state"
    ]]

    df.to_csv("C:/Users/shruti/Documents/projects/ecommerce-behaviour-analysis/data/processed/cleaned_data.csv", index=False)
    print("Preprocessing done! Shape:", df.shape)
    return df

if __name__ == "__main__":
    preprocess()