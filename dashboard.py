import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("AI Business Insight Dashboard")

# Load dataset
df = pd.read_csv("sales.csv", encoding="latin1")

# Sidebar filter
st.sidebar.header("Filters")
region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

filtered_df = df[df["Region"].isin(region)]

st.subheader("Dataset Preview")
st.write(filtered_df.head())

# KPI Metrics
total_sales = filtered_df["Sales"].sum()
total_orders = filtered_df["Order ID"].nunique()

col1, col2 = st.columns(2)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Orders", total_orders)

# Sales by Region
st.subheader("Sales by Region")

region_sales = filtered_df.groupby("Region")["Sales"].sum()

fig, ax = plt.subplots()
region_sales.plot(kind="bar", ax=ax)
plt.ylabel("Sales")
plt.title("Sales by Region")

st.pyplot(fig)

# Top Products
st.subheader("Top 10 Products")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig2, ax2 = plt.subplots()
top_products.plot(kind="barh", ax=ax2)
plt.xlabel("Sales")

st.pyplot(fig2)