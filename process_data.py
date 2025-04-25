import pandas as pd
import Library.data_ingestion as data_ingestion
import Library.data_processing as data_processing
import Library.data_enrichment as data_enrichment


def process_data():
    # [x] - Get data from sales csv
    sales_data = pd.read_csv('sales_data.csv')
    print(sales_data, '\n')
    # [x] - Get json data
    product_data = pd.read_json('product_data.json', encoding='utf-8-sig')
    print(product_data)

    # Refactor imports
    data_ingestion.data_ingestion()

    data_processing.data_processing()

    data_enrichment.data_enrichment()

# [x] - Output data to `aggregated_report.csv`
    df = pd.DataFrame(list())
    df.to_csv('aggregated_report.csv')


process_data()
