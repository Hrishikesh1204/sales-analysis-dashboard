# ==========================================================
# SALES DATA ANALYSIS PROJECT
# Author: Hrishikesh
# Tools: Python, Pandas, Matplotlib, Seaborn
# ==========================================================

# =============================
# IMPORT LIBRARIES
# =============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
sns.set_theme(style="whitegrid")

pd.set_option("display.max_columns", None)

# =============================
# LOAD DATASET
# =============================

file = r"C:\Users\hrish\OneDrive\Desktop\Sales Analysis project\Sales_cleaned.xlsx"

df = pd.read_excel(file, sheet_name="Sales_cleaned.xlsx")

# =============================
# BASIC DATA EXPLORATION
# =============================

print("\nFIRST 5 ROWS")
print(df.head())

print("\nLAST 5 ROWS")
print(df.tail())

print("\nSHAPE")
print(df.shape)

print("\nCOLUMNS")
print(df.columns)

print("\nINFO")
print(df.info())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATES")
print(df.duplicated().sum())

print("\nUNIQUE VALUES")
print(df.nunique())

# =============================
# DATA TYPE CONVERSION
# =============================

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# =============================
# KPIs
# =============================

print("\n========== KPIs ==========")

print("Total Sales :", round(df["Sales"].sum(),2))

print("Total Profit :", round(df["Profit"].sum(),2))

print("Total Quantity :", df["Quantity"].sum())

print("Total Orders :", df["Order ID"].nunique())

print("Average Sales :", round(df["Sales"].mean(),2))

print("Average Profit :", round(df["Profit"].mean(),2))

# ==================================================
# VISUALIZATION 1
# SALES BY REGION
# ==================================================

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))

sns.barplot(
    x=region_sales.values,
    y=region_sales.index,
    hue=region_sales.index,
    palette="viridis",
    legend=False
)

plt.title("Sales by Region")
plt.xlabel("Sales")
plt.ylabel("Region")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 2
# PROFIT BY REGION
# ==================================================

profit_region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))

sns.barplot(
    x=profit_region.values,
    y=profit_region.index,
    hue=profit_region.index,
    palette="magma",
    legend=False
)

plt.title("Profit by Region")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 3
# SALES BY CATEGORY
# ==================================================

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values,
    hue=category_sales.index,
    palette="Set2",
    legend=False
)

plt.title("Sales by Category")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 4
# PROFIT BY CATEGORY
# ==================================================

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    x=category_profit.index,
    y=category_profit.values,
    hue=category_profit.index,
    palette="coolwarm",
    legend=False
)

plt.title("Profit by Category")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 5
# SALES BY SUB CATEGORY
# ==================================================

subcategory = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=subcategory.values,
    y=subcategory.index,
    hue=subcategory.index,
    palette="Spectral",
    legend=False
)

plt.title("Sales by Sub Category")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 6
# SALES BY SEGMENT
# ==================================================

segment = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    segment,
    labels=segment.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales by Segment")

plt.show()

# ==================================================
# VISUALIZATION 7
# MONTHLY SALES
# ==================================================

monthly = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

monthly.index = monthly.index.astype(str)

plt.figure(figsize=(12,5))

plt.plot(
    monthly.index,
    monthly.values,
    marker="o",
    linewidth=2
)

plt.xticks(rotation=90)

plt.title("Monthly Sales Trend")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 8
# TOP 10 CUSTOMERS
# ==================================================

top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=top_customers.values,
    y=top_customers.index,
    hue=top_customers.index,
    palette="Blues_r",
    legend=False
)

plt.title("Top 10 Customers")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 9
# TOP 10 PRODUCTS
# ==================================================

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=top_products.values,
    y=top_products.index,
    hue=top_products.index,
    palette="rocket",
    legend=False
)

plt.title("Top 10 Products")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 10
# SALES DISTRIBUTION
# ==================================================

plt.figure(figsize=(8,5))

sns.histplot(df["Sales"], bins=30)

plt.title("Sales Distribution")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 11
# PROFIT DISTRIBUTION
# ==================================================

plt.figure(figsize=(8,5))

sns.boxplot(x=df["Profit"])

plt.title("Profit Distribution")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 12
# CORRELATION HEATMAP
# ==================================================

plt.figure(figsize=(8,6))

sns.heatmap(
    df[["Sales","Profit","Quantity","Discount"]].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

# ==================================================
# VISUALIZATION 13
# DISCOUNT VS PROFIT
# ==================================================

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit"
)

plt.title("Discount vs Profit")

plt.tight_layout()
plt.show()

# ==================================================
# BUSINESS INSIGHTS
# ==================================================

print("\n========== BUSINESS INSIGHTS ==========")

print("1. West region generated the highest sales.")

print("2. Technology category contributed the highest revenue.")

print("3. Consumer segment accounted for the largest share of sales.")

print("4. Monthly sales show seasonal fluctuations.")

print("5. Higher discounts often reduce profitability.")

print("6. A few customers contribute significantly to total sales.")

print("7. Some products generate high sales but relatively low profit.")

print("\nPROJECT COMPLETED SUCCESSFULLY")