
import sqlite3
import pandas as pd

# Read the CSV file
df = pd.read_csv("data/sales.csv")

# Connect to SQLite (creates the database if needed)
connection = sqlite3.connect("data/retail_sales.db")

# Load the sales data into a database table
df.to_sql("sales", connection, if_exists="replace", index=False)

print("Sales data loaded successfully!")

# Verify the number of records
count = pd.read_sql_query(
    "SELECT COUNT(*) AS total_orders FROM sales",
    connection
)

print(count.to_string(index=False))

connection.close()
