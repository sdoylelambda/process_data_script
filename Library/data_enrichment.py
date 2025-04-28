import pandas as pd
# [] - Enrich the sales data by merging it with product information using product IDs as keys.
#     [] - Handle any discrepancies or conflicts in the data.


def data_enrichment(product_data):
    print('data_enrichment')
    df = pd.read_csv('sales_data.csv')  # redundant get from ingestion

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
    df.to_csv('data_ingestion_dates.csv', index=False)
    print(f"Updated CSV saved to {'data_ingestion_date_updated.csv'}")