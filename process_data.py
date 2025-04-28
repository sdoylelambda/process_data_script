import pandas as pd
from Library.data_ingestion import DataIngestion
from Library.data_processing import data_processing
import json


def process_data():
    # user_input = input("Do you want to play a game?")
    #
    # print(user_input)

    ingestion = DataIngestion()

    # Update self.sales_data
    sales_data = ingestion.load_sales_data('sales_data.csv')
    product_data_loaded = ingestion.load_product_data('product_data.json')

    data_processing(product_data_loaded)

    # data_enrichment.data_enrichment()  --> call here (Not from processing, move date validation first)


# Assemble Final Output

# [] - Move to enrichment

# Load JSON list and convert to dict
with open('product_data.json', 'r') as json_file:
    product_list = json.load(json_file)

# Convert list of dicts to {product_id: category}
product_data = {item["product_id"]: item["category"] for item in product_list}

# Load sales CSV
sales_df = pd.read_csv('data_ingestion_date_updated.csv')  # Must contain: product_id, sale_amount, quantity

# Map category into sales_df
sales_df['category'] = sales_df['product_id'].map(product_data)

# Now group by product_id and category
product_agg = sales_df.groupby(['product_id', 'category']).agg(
    total_sales=('sale_amount', 'sum'),
    total_quantity=('quantity', 'sum')
).reset_index()

# For products: total_transactions = total_quantity (i.e., number of units sold)

# UPDATE --->

product_agg['total_transactions'] = product_agg['total_quantity']

# Now group by category
final_agg = product_agg.groupby('category').agg(
    total_sales=('total_sales', 'sum'),
    total_transactions=('total_transactions', 'sum'),
    total_quantity=('total_quantity', 'sum')
).reset_index()

# Calculate average_transaction_value
final_agg['average_transaction_value'] = final_agg['total_sales'] / final_agg['total_transactions']

# Round numeric columns
final_agg['total_sales'] = final_agg['total_sales'].round(2)
final_agg['average_transaction_value'] = final_agg['average_transaction_value'].round(2)

# Reorder columns
final_agg = final_agg[
    ['category', 'total_sales', 'total_transactions', 'average_transaction_value', 'total_quantity']
]

# Sort alphabetically by category
final_agg = final_agg.sort_values(by='category')

# Save to CSV
output_filename = 'aggregated_report.csv'
final_agg.to_csv(output_filename, index=False)

print(f"CSV file '{output_filename}' has been created and sorted alphabetically by category.")


process_data()
