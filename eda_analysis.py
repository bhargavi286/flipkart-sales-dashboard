import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('final_output_cleaned.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')  
df['Month'] = df['Date'].dt.to_period('M')  
monthly_sales = df.groupby('Month')['Revenue'].sum().reset_index()
plt.figure(figsize=(8, 5))
plt.plot(monthly_sales['Month'].astype(str), monthly_sales['Revenue'], marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
region_sales = df.groupby('Region')['Revenue'].sum().reset_index()
plt.figure(figsize=(6, 4))
plt.bar(region_sales['Region'], region_sales['Revenue'], color='skyblue')
plt.title("Region-wise Revenue")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
category_sales = df.groupby('Category')['Revenue'].sum().reset_index()
plt.figure(figsize=(6, 4))
plt.bar(category_sales['Category'], category_sales['Revenue'], color='orange')
plt.title("Category-wise Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
summary = df.groupby(['Region', 'Category'])['Revenue'].sum().reset_index()
print("\nRevenue by Region and Category:")
print(summary)
summary.to_csv('summary.csv', index=False)
print(" Summary exported to summary.csv")
