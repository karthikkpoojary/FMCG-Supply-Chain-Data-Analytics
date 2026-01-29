import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading Cleaned Data
@st.cache_data
def load_data():
    products = pd.read_csv("../data/cleaned/products.csv")
    inventory = pd.read_csv("../data/cleaned/inventory.csv")
    orders = pd.read_csv("../data/cleaned/orders.csv")
    forecast = pd.read_csv("../data/cleaned/demand_forecast.csv")
    return products, inventory, orders, forecast

products, inventory, orders, forecast = load_data()

#App Title & Sidebar Filters
st.title("📦 FMCG Supply Chain Analytics Dashboard")
st.markdown("Interactive tool for inventory, demand & logistics insights")

st.sidebar.header("Filters")

selected_product = st.sidebar.selectbox(
    "Select Product",
    products["product_id"].unique()
)

selected_warehouse = st.sidebar.selectbox(
    "Select Warehouse",
    inventory["warehouse"].unique()
)


#Section 1: Inventory & Stockout Analysis
st.subheader("📊 Inventory & Stockout Analysis")

#Filter inventory data:
filtered_inventory = inventory[
    (inventory["product_id"] == selected_product) &
    (inventory["warehouse"] == selected_warehouse)
]

#Stockout Count:
stockout_days = (filtered_inventory["stock_level"] == 0).sum()
st.metric("Stockout Days", stockout_days)

#Inventory Trend Chart
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(filtered_inventory["date"], filtered_inventory["stock_level"])
ax.set_title("Inventory Level Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Stock Level")

st.pyplot(fig)


#Section 2: Demand Forecast vs Actual
st.subheader("📈 Demand Forecast vs Actual")

#Filter forecast data:
filtered_forecast = forecast[
    forecast["product_id"] == selected_product
]
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(filtered_forecast["month"], filtered_forecast["actual_demand"], label="Actual", marker="o")
ax.plot(filtered_forecast["month"], filtered_forecast["forecast_qty"], label="Forecast", linestyle="--")
ax.legend()
ax.set_title("Forecast vs Actual Demand")

st.pyplot(fig)


#Section 3: Delivery Performance
st.subheader("🚚 Delivery Performance")

#Filter orders:
filtered_orders = orders[
    orders["product_id"] == selected_product
]

#Average Lead Time
avg_lead_time = filtered_orders["lead_time_days"].mean()
st.metric("Average Lead Time (Days)", round(avg_lead_time, 2))

#Lead Time Distribution
fig, ax = plt.subplots(figsize=(6,4))
sns.histplot(filtered_orders["lead_time_days"], bins=10, ax=ax)
ax.set_title("Lead Time Distribution")

st.pyplot(fig)

st.subheader("🧠 Business Summary")

st.write(f"""
- Product **{selected_product}** in **{selected_warehouse}** warehouse  
- Stockout Days: **{stockout_days}**  
- Avg Lead Time: **{round(avg_lead_time,2)} days**  

This combination helps identify **inventory risk and delivery inefficiencies**.
""")
