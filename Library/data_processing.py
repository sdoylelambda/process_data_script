import pandas as pd
import json

# [] - Normalize the data
#     [] - standardizing date formats
#     [] - product codes
#     [] - etc.


def data_processing(product_data):
    # [x] find missing data
    # [x] find that price in product_data.json
    # [x] find associated product_id in product_data.json

    print('data_processing')
    # Load CSV file
    df = pd.read_csv('sales_data.csv')  # redundant get from ingestion

    # Load JSON --- redundant get from ingestion
    with open('product_data.json', 'r') as f:
        product_data = json.load(f)

        # Create a mapping from sale_amount to product_id
    sale_to_product = {
        item['price']: item['product_id']
        for item in product_data
        if 'price' in item and 'product_id' in item
    }

    # Fill NaNs in 'product_id' by matching 'sale_amount'
    def fill_missing_id(row):
        if pd.isna(row['product_id']):
            return sale_to_product.get(row['sale_amount'], None)
        return row['product_id']

    df['product_id'] = df.apply(fill_missing_id, axis=1)

    # Save the updated CSV
    df.to_csv('data_ingestion.csv', index=False)
    print(f"Updated CSV saved to {'data_ingestion.csv'}")

    #     [] - correcting data types



    # This works but should be after date is fixed to prevent error - Validation

    # def process_data():
    #     expected_dtypes = {
    #         'date': 'datetime64[ns]',
    #         'transaction_id': 'string',
    #         'product_id': 'string',
    #         'quantity': 'float64',
    #         'sale_amount': 'float64'
    #     }
    #
    #     data = pd.read_csv('data_ingestion.csv', dtype={
    #         'transaction_id': 'string',
    #         'product_id': 'string',
    #         'quantity': 'float64',
    #         'sale_amount': 'float64'
    #     }, parse_dates=['date'])
    #
    #     # Validate column data types
    #     for column, expected_dtype in expected_dtypes.items():
    #         actual_dtype = data[column].dtype
    #         if str(actual_dtype) != expected_dtype:
    #             raise TypeError(f"Column '{column}' has dtype '{actual_dtype}' but expected '{expected_dtype}'")
    #
    #     print("All column data types are correct.")
    #
    # process_data()

    #     []  - ensure consistency
