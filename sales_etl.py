import pandas as pd

# Extract: Read sales data from CSV
df = pd.read_csv("sample_sales.csv")

print("Original Sales Data:")
print(df)

# Transform: Remove duplicates and invalid records
df = df.drop_duplicates()
df = df.dropna()

df = df[df["quantity"] > 0]
df = df[df["price"] >= 0]

# Calculate total sales
df["total_sales"] = df["quantity"] * df["price"]

# Load: Save processed data
df.to_csv("processed_sales.csv", index=False)

print("\nProcessed Sales Data:")
print(df)

print("\nTotal Revenue:", df["total_sales"].sum())
print("ETL pipeline completed successfully!")
