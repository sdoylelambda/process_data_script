import csv
import numpy as np
import pandas as pd
import json


# [] - Clean sales data

def data_ingestion():  # redundant
    # Load CSV
    sales = pd.read_csv('sales_data.csv')

    # Load JSON
    with open('product_data.json', 'r') as f:
        product_data = json.load(f)

    return sales, product_data
