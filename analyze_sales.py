
import pandas as pd
import matplotlib.pyplot as plt

# Load the retail sales dataset
df = pd.read_csv("data/sales.csv")

# Calculate revenue and profit for each order
df["revenue"] = df["units_sold"] * df["unit_price"]
df["profit"] = df["units_sold"] * (
    df["unit_price"] - df["unit_cost"]
)

# Display a sample of the dataset
print("\n--- RETAIL SALES DATA ---")
print(df.head())

# Calculate overall business performance
total_revenue = df["revenue"].sum()
total_profit = df["profit"].sum()
total_units = df["units_sold"].sum()

print("\n--- BUSINESS SUMMARY ---")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Units Sold: {total_units}")

# Compare sales by product category
category_summary = df.groupby("category").agg(
    revenue=("revenue", "sum"),
    profit=("profit", "sum"),
    units_sold=("units_sold", "sum")
).sort_values("revenue", ascending=False)

print("\n--- PERFORMANCE BY CATEGORY ---")
print(category_summary.to_string())

# Compare revenue by region
region_summary = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- REVENUE BY REGION ---")
print(region_summary.to_string())

# Identify products with low inventory
# Use the latest recorded stock level for each product
df["order_date"] = pd.to_datetime(df["order_date"])

latest_stock = (
    df.sort_values("order_date")
    .drop_duplicates(subset="product", keep="last")
    [["product", "stock_remaining"]]
)

low_stock = latest_stock[
    latest_stock["stock_remaining"] < 10
]

print("\n--- LOW INVENTORY PRODUCTS ---")
print(low_stock.to_string(index=False))

# Create a revenue chart by category
plt.figure(figsize=(8, 5))
plt.bar(category_summary.index, category_summary["revenue"])

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue ($)")
plt.tight_layout()

plt.savefig("data/revenue_by_category.png", dpi=300)
plt.show()

print("\nChart saved to data/revenue_by_category.png")

# Analyze monthly revenue trends
df["month"] = df["order_date"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("month")["revenue"]
    .sum()
    .sort_index()
)

print("\n--- MONTHLY REVENUE ---")
print(monthly_sales.to_string())

# Create a monthly revenue trend chart
plt.figure(figsize=(9, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("data/monthly_revenue_trend.png", dpi=300)
plt.show()

print("\nChart saved to data/monthly_revenue_trend.png")
