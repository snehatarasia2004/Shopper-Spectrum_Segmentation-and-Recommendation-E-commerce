## 📊 Data & Model Statistics

### 🧾 Dataset Overview

| Metric                    | Value                        |
| ------------------------- | ---------------------------- |
| **Total Transactions**    | \~541,909                    |
| **Unique Products**       | \~4,000+                     |
| **Unique Customers**      | \~38,000                     |
| **Transaction Period**    | Dec 2022 – Dec 2023          |
| **Countries Represented** | \~37                         |
| **Missing Customer IDs**  | \~24.9% of rows filtered out |

---

### 🧹 Data Cleaning Summary

| Action                               | Count Removed |
| ------------------------------------ | ------------- |
| Rows with Missing `CustomerID`       | \~135,000+    |
| Cancelled Invoices (`InvoiceNo` "C") | \~9,600+      |
| Negative/Zero Quantity or Price      | \~17,000+     |

---

### 📦 RFM Segmentation Stats

| RFM Metric       | Min  | Max    | Mean    |
| ---------------- | ---- | ------ | ------- |
| **Recency**      | 1    | 373    | \~92.6  |
| **Frequency**    | 1    | 209    | \~4.4   |
| **Monetary (£)** | 3.75 | 28000+ | \~440.3 |

---

### 🤖 KMeans Clustering

| Metric               | Value                                    |
| -------------------- | ---------------------------------------- |
| **Algorithm**        | KMeans (Scikit-learn)                    |
| **Features Used**    | RFM (scaled)                             |
| **Optimal Clusters** | 4                                        |
| **Silhouette Score** | \~0.46                                   |
| **Cluster Labels**   | High-Value, Regular, Occasional, At-Risk |

| Cluster # | Segment Label | % of Customers |
| --------- | ------------- | -------------- |
| 0         | High-Value    | \~8–10%        |
| 1         | Regular       | \~30%          |
| 2         | Occasional    | \~45%          |
| 3         | At-Risk       | \~15%          |

---

### 💼 Product Recommendation

| Metric                          | Value                                     |
| ------------------------------- | ----------------------------------------- |
| **Technique**                   | Item-based Collaborative Filtering        |
| **Similarity Metric**           | Cosine Similarity                         |
| **Recommendations per Product** | Top 5                                     |
| **Matrix Shape**                | \~38,000 (Customers) x \~3,900 (Products) |
| **Average Products Purchased**  | \~7–10 per customer                       |

---

### 📋 Streamlit App Summary

| Module                | Features                                     |
| --------------------- | -------------------------------------------- |
| Product Recommender   | Input product → Recommends 5 similar items   |
| Customer Segmentation | Input RFM values → Predicts customer segment |
| Backend Models        | `kmeans_model.joblib`, `product_matrix.pkl`  |
| Frontend Tool         | Built with Streamlit                         |
