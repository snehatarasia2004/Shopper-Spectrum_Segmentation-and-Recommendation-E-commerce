import streamlit as st
import pandas as pd
import joblib
from sklearn.neighbors import NearestNeighbors
import requests
import io
import gdown
import os

# --- Load CSV from Google Drive ---
st.info("📥 Loading retail data from Google Drive...")
csv_url =https://drive.google.com/file/d/1rzRwxm_CJxcRzfoo9Ix37A2JTlMummY-/view?usp=drive_link

try:
    response = requests.get(csv_url)
    response.raise_for_status()
    df = pd.read_csv(io.StringIO(response.text), encoding="ISO-8859-1", on_bad_lines='skip')
    st.success("✅ Retail data loaded.")
except Exception as e:
    st.error(f"❌ Error loading retail data: {e}")
    st.stop()

# --- Clean data ---
df.dropna(subset=["CustomerID", "Description", "Quantity", "UnitPrice", "InvoiceDate"], inplace=True)
df["Description"] = df["Description"].astype(str).str.strip().str.upper()
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["TotalSum"] = df["Quantity"] * df["UnitPrice"]

# --- Download product_matrix.pkl from Google Drive ---
file_id = "1i9Q3LqmAjTjOvUBpp66Y3rsXpXo392KX"
output_file = "product_matrix.pkl"

# Download only if not already present
if not os.path.exists(output_file):
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output_file, quiet=False)

# Load the file
product_matrix = joblib.load(output_file)

# --- Load Product Matrix Safely ---
try:
    product_matrix = joblib.load(output_file)
    st.success("✅ Product matrix loaded.")
except Exception as e:
    st.error(f"❌ Error loading product_matrix.pkl: {e}")
    st.stop()
# --- RFM Table for Customer Segmentation ---
snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
rfm_df = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalSum": "sum"
}).reset_index()

rfm_df.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]
rfm_df.dropna(inplace=True)

# --- Load pre-trained KMeans model ---
kmeans = joblib.load("kmeans_model.joblib")

# --- Sidebar ---
st.sidebar.title("🛍️ Shopper Spectrum")
module = st.sidebar.radio("Select Module", ["1️⃣ Product Recommender", "2️⃣ Customer Segmentation"])

# --- Product Recommender ---
if module.startswith("1️"):
    st.title("🎯 Product Recommender")

    # Dropdown for safe selection
    product_list = sorted(product_matrix.columns.tolist())
    selected_product = st.selectbox("🔍 Select a Product", product_list)

    if st.button("🔄 Recommend Similar Products"):
        try:
            # Create model and fit
            model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
            model_knn.fit(product_matrix.T.values)

            # Find index of selected product
            product_idx = list(product_matrix.columns).index(selected_product)
            distances, indices = model_knn.kneighbors([product_matrix.T.values[product_idx]], n_neighbors=6)

            st.success("🛒 Recommended Products:")
            for idx in indices.flatten()[1:]:
                st.write(f"• {product_matrix.columns[idx].title()}")
        except ValueError:
            st.error("❌ Product not found. Please select a valid product from the list.")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
# --- Customer Segmentation ---
elif module.startswith("2️"):
   import streamlit as st
import numpy as np
import joblib

# Load trained clustering model
kmeans_model = joblib.load("kmeans_model.joblib")

# Define segment mapping based on cluster number (update based on your model's cluster labels)
segment_labels = {
    0: "High-Value",
    1: "Regular",
    2: "Occasional",
    3: "At-Risk"
}

st.set_page_config(page_title="Customer Segmentation", page_icon="👥")
st.title("🎯 2️⃣ Customer Segmentation Module")
st.markdown("🔍 Predict the customer segment using RFM inputs")

# --- Input fields ---
recency = st.number_input("🕒 Recency (days since last purchase)", min_value=0, value=30)
frequency = st.number_input("🔁 Frequency (number of purchases)", min_value=0, value=5)
monetary = st.number_input("💰 Monetary (total spend)", min_value=0.0, value=200.0, step=10.0)

# --- Predict button ---
if st.button("📊 Predict Cluster"):
    rfm_input = np.array([[recency, frequency, monetary]])
    cluster = kmeans_model.predict(rfm_input)[0]

    segment = segment_labels.get(cluster, f"Cluster {cluster}")
    st.success(f"✅ This customer belongs to segment: **{segment}**")
