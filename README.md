# Monthly Sales Analysis – PASD 2025 Mini-Project

This repository contains my mini-project for the course **Python avancé pour la science des données (AP_DS)**.

The goal of the project is to **simulate monthly sales for four products over one year**, analyse the data with **NumPy & Pandas**, and build clear **visualisations** with **Matplotlib & Seaborn** to extract simple business insights (best product, best month, best quarter, etc.).

---

## 1. Project Overview

The project follows a typical **data analysis workflow**:

1. Generate a **synthetic sales dataset** for 4 products (A, B, C, D) over 12 months.
2. Build a **Pandas DataFrame** with time-based features:
   - Month name / month number  
   - Quarter (Q1–Q4)
3. Compute analysis metrics:
   - `Total_Sales` per month  
   - `Average_Sales` per month  
   - `Month_over_Month_Growth` (percentage)
   - `Max_Sales_Product` and `Min_Sales_Product` per month
4. Use **pivot tables** to summarise results at the quarterly level.
5. Visualise the data with:
   - Line chart (monthly trends per product)
   - Stacked bar chart (total monthly sales, by product)
   - Heatmap (months × products)
   - Boxplot (distribution of sales per product)
6. Export intermediate and final results as CSV files.

The dataset is **fully synthetic** (randomly generated), but the workflow is the same as with real business data.

---

## 2. Project Structure

```text
project_sales/
├── README.md           # Project documentation (this file)
├── notebook.ipynb      # Main analysis notebook (code + plots + comments)
├── utils.py            # Helper functions to generate synthetic sales data
└── data/
    ├── initial.csv     # Raw generated data (monthly sales per product)
    ├── final.csv       # Enriched DataFrame with metrics and extra features
    └── output.csv      # Pivot tables / quarterly summaries
