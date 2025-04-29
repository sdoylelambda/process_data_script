import pandas as pd
import pytest


def process_sales_data(sales_df, product_list):
    # Map product_id -> category
    product_data = {item["product_id"]: item["category"] for item in product_list}
    sales_df['category'] = sales_df['product_id'].map(product_data)

    # If quantity not provided, default to 1
    if 'quantity' not in sales_df.columns:
        sales_df['quantity'] = 1

    # Group directly by category
    final_agg = sales_df.groupby('category').agg(
        total_sales=('sale_amount', 'sum'),
        total_quantity=('quantity', 'sum'),
        total_transactions=('quantity', 'sum')
    ).reset_index()

    final_agg['average_transaction_value'] = final_agg['total_sales'] / final_agg['total_transactions']

    final_agg['total_sales'] = final_agg['total_sales'].round(2)
    final_agg['average_transaction_value'] = final_agg['average_transaction_value'].round(2)

    final_agg = final_agg[
        ['category', 'total_sales', 'total_transactions', 'average_transaction_value', 'total_quantity']
    ]

    final_agg = final_agg.sort_values(by='category')

    return final_agg


def test_process_sales_data():
    # Mock sales data
    sales_data = pd.DataFrame({
        'product_id': ['p1', 'p1', 'p2', 'p3'],
        'sale_amount': [100.00, 50.00, 75.00, 40.00],
        'quantity': [2, 1, 3, 1]
    })

    # Mock product JSON list
    product_list = [
        {'product_id': 'p1', 'category': 'Gadgets'},
        {'product_id': 'p2', 'category': 'Books'},
        {'product_id': 'p3', 'category': 'Accessories'}
    ]

    # Process the data
    result = process_sales_data(sales_data, product_list)

    # Expected data
    expected_data = pd.DataFrame({
        'category': ['Accessories', 'Books', 'Gadgets'],
        'total_sales': [40.00, 75.00, 150.00],
        'total_transactions': [1, 3, 3],
        'average_transaction_value': [40.00, 25.00, 50.00],
        'total_quantity': [1, 3, 3]
    })

    # Make sure column order matches
    result = result.reset_index(drop=True)
    expected_data = expected_data.reset_index(drop=True)

    # Check columns
    assert list(result.columns) == list(expected_data.columns), "Column names or order mismatch."

    # Check all values
    pd.testing.assert_frame_equal(result, expected_data)
