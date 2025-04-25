import pandas as pd
import numpy as np
import Library.data_ingestion as data_ingestion
import Library.data_processing as data_processing
import Library.data_enrichment as data_enrichment
import csv


def process_data():
    # x = input("Do you want to play a game?")
    #
    # print(x)
    #
    # with open("sales_data.csv") as file:
    #     rows = list(csv.reader(file))
    #     if rows[2] == '':
    #         rows[2] = 44444
    # print(rows)

    # with open('sales_data.csv', 'r') as file:
    #     reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    #     data = []
    #     for row in reader:
    #         row = [value if value is not None else 0 for value in row]
    #         data.append(row)
    # print(data)






































    # print(sales_data)

    # [x] - Get json data
    product_data = pd.read_json('product_data.json', encoding='utf-8-sig')
    # print(product_data)

    # Refactor imports
    # data_ingestion.data_ingestion()  use this instead of pulling from data_processing

    data_processing.data_processing(product_data)

    # data_enrichment.data_enrichment()

# [x] - Output data to `aggregated_report.csv`
    df = pd.DataFrame(list())
    df.to_csv('aggregated_report.csv')


process_data()
