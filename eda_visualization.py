import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("final_output_cleaned.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Monthly Revenue Trend
df["Month"] = df["Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month")["Revenue"].sum().reset_index()

plt.figure(figsize=(8, 4))
sns.lineplot(data=monthly, x="Month", y="Revenue", marker='o')
plt.title("Monthly Revenue Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()

# Revenue by Region
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="Region", y="Revenue", estimator=sum)
plt.title("Total Revenue by Region")
plt.tight_layout()
plt.savefig("revenue_by_region.png")
plt.close()

# Revenue by Product Category
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="Category", y="Revenue", estimator=sum)
plt.title("Total Revenue by Category")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.close()

print("✅ EDA visualizations saved as PNGs.")

