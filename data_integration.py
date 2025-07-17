import pandas as pd
import json

# Load data
sales_df = pd.read_csv("sales_data.csv")
with open("product_metadata.json") as f:
    product_data = json.load(f)
product_df = pd.DataFrame(product_data)
region_df = pd.read_excel("region_info.xlsx")

# Merge
merged = pd.merge(sales_df, product_df, on="Product", how="left")
final_df = pd.merge(merged, region_df, on="Region", how="left")
final_df.to_csv("final_output.csv", index=False)

print(" Data integration completed.")
print(final_df.head())
