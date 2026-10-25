import pandas as pd

# Extract: Create sample sales data
data = {
    "order_id": [101, 102, 103, 104, 105],
    "product": ["Laptop", "Phone", "Tablet", "Phone", "Laptop"],
    "quantity": [2, 3, 1, 2, 1],
    "price": [50000, 15000, 20000, 15000, 50000]
}

df = pd.DataFrame(data)

# Transform: Calculate total sales
df["total_sales"] = df["quantity"] * df["price"]

# Data quality: Remove duplicate records
df = df.drop_duplicates()

# Load: Save processed data to CSV
df.to_csv("processed_sales.csv", index=False)

print("Sales ETL pipeline completed successfully!")
print(df)
