import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("C:/Users/shruti/Documents/projects/ecommerce-behaviour-analysis/data/processed/cleaned_data.csv")

# --- Customer Segmentation (K-Means) ---
features = df[["total_spend", "tenure", "payment_installments"]]
kmeans = KMeans(n_clusters=4, random_state=42)
df["segment"] = kmeans.fit_predict(features)
df.to_csv("data/processed/segmented_data.csv", index=False)
print("Segmentation done!")

# --- High Value Customer Prediction (Random Forest) ---
df["high_value"] = (df["total_spend"] > df["total_spend"].median()).astype(int)
X = df[["tenure", "payment_installments", "price", "freight_value"]]
y = df["high_value"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))
joblib.dump(model, "models/rf_model.pkl")
print("Model saved!")