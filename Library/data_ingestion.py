import pandas as pd
import os


class DataIngestion:
    def __init__(self):
        pass

    def load_sales_data(self, filepath: str) -> pd.DataFrame:
        """Load sales data from a CSV file."""
        self._validate_file(filepath)
        return pd.read_csv(filepath)

    def load_product_data(self, filepath: str) -> pd.DataFrame:
        """Load product data from a JSON file."""
        self._validate_file(filepath)
        return pd.read_json(filepath, encoding='utf-8-sig')

    def _validate_file(self, filepath: str):
        """Check if a file exists and is not empty."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        if os.path.getsize(filepath) == 0:
            raise ValueError(f"File is empty: {filepath}")
