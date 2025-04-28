import pandas as pd
from datetime import datetime
from Library import data_enrichment


def normalize_date(date_str: str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except (ValueError, TypeError):
        pass

    possible_formats = [
        "%d-%m-%Y",
        "%m-%d-%Y",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%Y/%m/%d",
        "%d.%m.%Y",
        "%B %d, %Y",
        "%b %d, %Y",
    ]

    for fmt in possible_formats:
        try:
            parsed_date = datetime.strptime(str(date_str), fmt)
            return parsed_date.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            continue

    return None  # If unrecognized, return None


def normalize_dates_in_csv(input_file, output_file):
    df = pd.read_csv(input_file)

    # Apply normalization to the first column
    first_col = df.columns[0]
    df[first_col] = df[first_col].apply(normalize_date)

    # Drop rows where date could not be parsed (optional)
    df = df.dropna(subset=[first_col])

    # Save to output
    df.to_csv(output_file, index=False)


def data_processing(product_data):
    print('data_processing')

    # Probably want to call this at the end -> Update date check to run last
    data_enrichment.data_enrichment(product_data)  # Update this import

    # Fix Date Format
    normalize_dates_in_csv('data_ingestion.csv', 'data_ingestion_date_updated.csv')

    def process_data():
        expected_dtypes = {
            'date': 'datetime64[ns]',
            'transaction_id': 'string',
            'product_id': 'string',
            'quantity': 'float64',
            'sale_amount': 'float64'
        }

        data = pd.read_csv('data_ingestion_date_updated.csv', dtype={
            'transaction_id': 'string',
            'product_id': 'string',
            'quantity': 'float64',
            'sale_amount': 'float64'
        }, parse_dates=['date'])

        # Validate column data types
        for column, expected_dtype in expected_dtypes.items():
            actual_dtype = data[column].dtype
            if str(actual_dtype) != expected_dtype:
                raise TypeError(f"Column '{column}' has dtype '{actual_dtype}' but expected '{expected_dtype}'")

        print("All column data types are correct.")

    process_data()
