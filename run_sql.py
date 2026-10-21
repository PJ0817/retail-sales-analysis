
import sqlite3

# Connect to the retail database
connection = sqlite3.connect("data/retail_sales.db")

# Read the SQL file
with open("sales_analysis.sql", "r") as file:
    sql_script = file.read()

# Run each query separately so we can display its results
queries = [q.strip() for q in sql_script.split(";") if q.strip()]

for number, query in enumerate(queries, start=1):
    print(f"\n--- SQL QUERY {number} ---")
    cursor = connection.execute(query)

    if cursor.description:
        columns = [column[0] for column in cursor.description]
        print(" | ".join(columns))

        for row in cursor.fetchall():
            print(" | ".join(str(value) for value in row))

connection.close()
