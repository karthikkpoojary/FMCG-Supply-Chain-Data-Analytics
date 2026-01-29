---
# 🧑‍💻 CODE WALKTHROUGH – FMCG Supply Chain Analytics

![Python](https://img.shields.io/badge/Python-Code-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?logo=jupyter)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)


## 📌 Purpose of This File

This document explains:
- What each notebook and script does
- Why certain logic was used
- How the analysis flows step-by-step

It is written for **interviewers, reviewers, and collaborators**.


## 📁 1. Data Creation & Cleaning  
📓 `01_data_creation_and_cleaning.ipynb`

### Key Tasks
- Created **synthetic FMCG supply chain data**
- Simulated real-world scenarios like stockouts & delays
- Cleaned missing values and duplicates
- Engineered lead-time features

### Key Libraries
```
pandas
numpy
```

### Output
- Cleaned CSV files saved to `/data/cleaned/`


## 📁 2. Exploratory Data Analysis (EDA)

📓 `02_supply_chain_eda.ipynb`

Business Questions Answered

- Where do stockouts occur?
- Which products are overstocked?
- Which warehouses perform poorly?
- How severe are delivery delays?

Analysis Techniques

- GroupBy aggregations
- Time-series trends
- Bar charts & distributions
- Product & warehouse comparisons


## Key Libraries
```
pandas
matplotlib
seaborn
```


## 📁 3. Demand Forecasting

📓 `03_demand_forecasting.ipynb`

Forecasting Methods Used

- 📈 Moving Average (primary)
- 📉 Linear Regression (trend-based)

Metrics Evaluated

- Forecast Error
- Mean Absolute Error (MAE)

Business Logic

- Under-forecast → stockout risk
- Over-forecast → overstock risk


## 📁 4. Inventory Optimization Logic

Concepts Implemented

- Reorder Point (ROP)
- Safety Stock calculation

Logic Used
- ```Reorder Point = (Avg Daily Demand × Lead Time) + Safety Stock```


## 📁 5. Power BI Dashboard

Measures Created (DAX)

- Total Orders
- Average Lead Time
- Stockout Days
- Forecast Error
- Average Inventory

Dashboard Design

- Executive-friendly visuals
- Minimal clutter
- KPI-driven storytelling


## 📁 6. Streamlit Application

📄 `streamlit_app/app.py`

Features

- Product & warehouse filters
- Inventory trend visualization
- Forecast vs actual demand comparison
- Delivery performance monitoring

## Libraries Used
```
streamlit
pandas
matplotlib
seaborn
```

## Run Command
```
streamlit run app.py
```


## 🧠 Design Philosophy

- Business-first approach
- Simple, explainable logic
- Interview-friendly code
- Scalable structure

## ✅ What This Project Demonstrates

- Ability to convert business problems into data solutions
- Strong fundamentals in supply chain analytics
- Clear understanding of inventory & forecasting concepts
- End-to-end project ownership


## 📌 Note to Reviewers

This project was intentionally designed to reflect real FMCG supply chain challenges and not just academic exercises.

