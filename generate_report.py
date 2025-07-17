import pandas as pd
import pdfkit
from jinja2 import Environment, FileSystemLoader
df = pd.read_csv('final_output_cleaned.csv')
summary = pd.read_csv('summary.csv')
total_revenue = df['Revenue'].sum()
top_region = df.groupby('Region')['Revenue'].sum().idxmax()
top_category = df.groupby('Category')['Revenue'].sum().idxmax()
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("report_template.html")
html_out = template.render(
    total_revenue=total_revenue,
    top_region=top_region,
    top_category=top_category,
    summary_table=summary.to_html(index=False)
)
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
pdfkit.from_string(html_out, "sales_report.pdf", configuration=config)
print(" PDF report generated: sales_report.pdf")
