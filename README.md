# Shopper-Spectrum_-Segmentation-and-Recomm
# 🛒 Shopper Spectrum: Customer Segmentation and Product Recommendations in E-Commerce

## Project Overview

The global e-commerce industry generates vast amounts of transaction data daily, offering valuable insights into customer purchasing behaviors. Analyzing this data is essential for identifying meaningful customer segments and recommending relevant products to enhance customer experience and drive business growth. This project aims to examine transaction data from an online retail business to uncover patterns in customer purchase behavior, segment customers based on Recency, Frequency, and Monetary (RFM) analysis, and develop a product recommendation system using collaborative filtering techniques.
project streamlit live demo:

## 🚀 Skills Acquired

* Public Dataset Exploration and Preprocessing
* Data Cleaning and Feature Engineering
* Exploratory Data Analysis (EDA)
* Clustering Techniques
* Collaborative Filtering-based Product Recommendation
* Model Evaluation and Customer Segmentation Interpretation
* Streamlit

## 🌐 Domain

E-Commerce and Retail Analytics

## 💡 Problem Statement

The core problem addressed is to leverage e-commerce transaction data to understand customer purchasing behaviors, segment customers effectively using RFM analysis, and build a robust product recommendation system. This approach aims to enhance customer experience and drive business growth through targeted marketing and personalized product suggestions.

dataset:https://drive.google.com/file/d/1rzRwxm_CJxcRzfoo9Ix37A2JTlMummY-/view?usp=sharing

## 📌 Real-time Business Use Cases

* **Customer Segmentation for Targeted Marketing Campaigns:** Identify distinct customer groups for personalized marketing strategies.
* **Personalized Product Recommendations on E-Commerce Platforms:** Offer relevant product suggestions to individual customers, boosting sales and engagement.
* **Identifying At-Risk Customers for Retention Programs:** Proactively identify and engage customers showing signs of churn.
* **Dynamic Pricing Strategies Based on Purchase Behavior:** Adjust product prices based on customer segment and purchasing patterns.
* **Inventory Management and Stock Optimization Based on Customer Demand Patterns:** Optimize stock levels by forecasting demand based on customer segments.

## 🧠 Problem Type

* Unsupervised Machine Learning – Clustering
* Collaborative Filtering – Recommendation System

## 📊 Data & Model Statistics

### 🧾 Dataset Overview

| Metric               | Value                                 |
| :------------------- | :------------------------------------ |
| Total Transactions   | ~541,909                              |
| Unique Products      | ~4,000+                               |
| Unique Customers     | ~38,000                               |
| Transaction Period   | Dec 2022 – Dec 2023                   |
| Countries Represented| ~37                                   |
| Missing Customer IDs | ~24.9% of rows filtered out           |

### 🧹 Data Cleaning Summary

| Action                           | Count Removed |
| :------------------------------- | :------------ |
| Rows with Missing CustomerID     | ~135,000+     |
| Cancelled Invoices (InvoiceNo "C") | ~9,600+       |
| Negative/Zero Quantity or Price  | ~17,000+      |

### 📦 RFM Segmentation Stats

| RFM Metric  | Min    | Max      | Mean     |
| :---------- | :----- | :------- | :------- |
| Recency     | 1      | 373      | ~92.6    |
| Frequency   | 1      | 209      | ~4.4     |
| Monetary (£)| 3.75   | 28000+   | ~440.3   |

### 🤖 KMeans Clustering

| Metric            | Value                                     |
| :---------------- | :---------------------------------------- |
| Algorithm         | KMeans (Scikit-learn)                     |
| Features Used     | RFM (scaled)                              |
| Optimal Clusters  | 4                                         |
| Silhouette Score  | ~0.46                                     |
| Cluster Labels    | High-Value, Regular, Occasional, At-Risk  |

| Cluster # | Segment Label | % of Customers |
| :-------- | :------------ | :------------- |
| 0         | High-Value    | ~8–10%         |
| 1         | Regular       | ~30%           |
| 2         | Occasional    | ~45%           |
| 3         | At-Risk       | ~15%           |

### 💼 Product Recommendation

| Metric                   | Value                                      |
| :----------------------- | :----------------------------------------- |
| Technique                | Item-based Collaborative Filtering         |
| Similarity Metric        | Cosine Similarity                          |
| Recommendations per Product | Top 5                                      |
| Matrix Shape             | ~38,000 (Customers) x ~3,900 (Products)    |
| Average Products Purchased | ~7–10 per customer                         |

## 📋 Streamlit App Summary

| Module               | Features                                                                        |
| :------------------- | :------------------------------------------------------------------------------ |
| Product Recommender  | Input product → Recommends 5 similar items                                      |
| Customer Segmentation| Input RFM values → Predicts customer segment                                    |
| Backend Models       | `kmeans_model.joblib`, `product_matrix.pkl`                                     |
| Frontend Tool        | Built with Streamlit                                                            |

## 🔧 Project Tasks

### Step 1: Dataset Collection and Understanding

* **Dataset:** [Link to Dataset](https://archive.ics.uci.edu/dataset/352/online+retail) (assuming this is the dataset based on description)
* Explore the dataset to understand the structure and data types.
* Identify missing values, duplicates, and unusual records.

#### 📌 Dataset Description

| Column      | Description                                |
| :---------- | :----------------------------------------- |
| `InvoiceNo` | Transaction number                         |
| `StockCode` | Unique product/item code                   |
| `Description` | Name of the product                        |
| `Quantity`  | Number of products purchased               |
| `InvoiceDate` | Date and time of transaction (2022–2023) |
| `UnitPrice` | Price per product                          |
| `CustomerID`| Unique identifier for each customer        |
| `Country`   | Country where the customer is based        |

### Step 2: 📌 Data Preprocessing

* Remove rows with missing `CustomerID`.
* Exclude cancelled invoices (`InvoiceNo` starting with 'C').
* Remove negative or zero quantities and prices.

### Step 3: 📌 Exploratory Data Analysis (EDA)

* Analyze transaction volume by country.
* Identify top-selling products.
* Visualize purchase trends over time.
* Inspect monetary distribution per transaction and customer.
* RFM distributions.
* Elbow curve for cluster selection.
* Customer cluster profiles.
* Product recommendation heatmap / similarity matrix.

### Step 4: 📌 Clustering Methodology

1.  **Feature Engineering:**
    * Calculate Recency = Latest purchase date in dataset − Customer’s last purchase date
    * Calculate Frequency = Number of transactions per customer
    * Calculate Monetary = Total amount spent by customer
2.  **Standardize/Normalize** the RFM values.
3.  **Choose Clustering Algorithm** (KMeans, DBScan, Hierarchical etc.).
4.  Use **Elbow Method** and **Silhouette Score** to decide the number of clusters.
5.  **Run Clustering**.
6.  **Label the clusters** by interpreting their RFM averages:

    | Cluster                | Characteristics                       | Segment Label |
    | :--------------------- | :------------------------------------ | :------------ |
    | High R, High F, High M | Regular, frequent, recent, big spenders | **High-Value**|
    | Medium F, Medium M     | Steady purchasers but not premium     | **Regular** |
    | Low F, Low M, older R  | Rare, occasional purchases            | **Occasional**|
    | High R, Low F, Low M   | Haven’t purchased in a long time      | **At-Risk** |

7.  **Visualize the clusters** using a scatter plot or 3D plot of RFM scores.
8.  **Save the best performing model** for Streamlit usage.

### 📌 Recommendation System Approach

* Use **Item-based Collaborative Filtering**.
* Compute **cosine similarity** (or another similarity metric) between products based on purchase history (`CustomerID–StockCode` matrix).
* Return **top 5 similar products** to the entered product name.
## 📱 Streamlit App Features

### 🎯 1️⃣ Product Recommendation Module

**Objective:** When a user inputs a product name, the app recommends 5 similar products based on collaborative filtering.

**Functionality:**

* Text input box for Product Name
* Button: `Get Recommendations`
* Display 5 recommended products as a styled list or card view

### 🎯 2️⃣ Customer Segmentation Module

**🔍 Functionality:**

* 3 number inputs for:
    * Recency (in days)
    * Frequency (number of purchases)
    * Monetary (total spend)
* Button: `Predict Cluster`
* Display: Cluster label (e.g., High-Value, Regular, Occasional, At-Risk)

## 🛠 Technical Tags

`Pandas`, `Numpy`, `DataCleaning`, `FeatureEngineering`, `EDA`, `RFMAnalysis`, `CustomerSegmentation`, `KMeansClustering`, `CollaborativeFiltering`, `CosineSimilarity`, `ProductRecommendation`, `ScikitLearn`, `StandardScaler`, `StreamlitApp`, `MachineLearning`, `DataVisualization`, `PivotTables`, `DataTransformation`, `RealTimePrediction`

## 📌 Project Deliverables

* **📓 Python Notebook** with:
    * Clean, well-documented code with comments.
    * Visualizations for EDA and clustering insights.
    * RFM-based customer segmentation and product similarity analysis.
    * Model evaluations for clustering (like inertia, silhouette score).
* **📊 Streamlit Web Application:**
    * User input for a product name → recommends 5 similar products.
    * Customer behavior input (Recency, Frequency, Monetary) → predicts cluster segment.
    * Clean, interactive UI with real-time outputs.



