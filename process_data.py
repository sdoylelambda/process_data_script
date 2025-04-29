import pandas as pd
import json
from Library.data_ingestion import DataIngestion
from Library.data_processing import data_processing


def process_data():
    user_input = input("Press 'Y' to create? ")

    if user_input.upper() != 'Y':
        print("Exiting process.")
        return

    # Load product data
    with open('product_data.json', 'r') as f:
        product_list = json.load(f)

    data_processing(product_list)

    product_data = {item["product_id"]: item["category"] for item in product_list}

    # Load sales data
    sales_df = pd.read_csv('sales_data.csv')  # <-- Use the correct CSV

    # Map category from product data
    sales_df['category'] = sales_df['product_id'].map(product_data)

    # Drop rows where product_id or category is missing
    sales_df = sales_df.dropna(subset=['product_id', 'category'])

    # Group by category
    final_agg = sales_df.groupby('category').agg(
        total_sales=('sale_amount', 'sum'),
        total_transactions=('transaction_id', 'nunique'),  # Count unique transactions
        total_quantity=('quantity', 'sum')
    ).reset_index()

    # Calculate average transaction value
    final_agg['average_transaction_value'] = final_agg['total_sales'] / final_agg['total_transactions']

    # Round the numbers
    final_agg['total_sales'] = final_agg['total_sales'].round(2)
    final_agg['average_transaction_value'] = final_agg['average_transaction_value'].round(2)

    # Reorder columns
    final_agg = final_agg[
        ['category', 'total_sales', 'total_transactions', 'average_transaction_value', 'total_quantity']
    ]

    # Sort by category
    final_agg = final_agg.sort_values('category')

    # Save to CSV
    final_agg.to_csv('aggregated_report.csv', index=False)

    print(f"CSV file 'aggregated_report.csv' has been created and sorted alphabetically by category.")


process_data()
