import pandas as pd
import pytest
from Library.data_ingestion import DataIngestion
import tempfile
import json
import os


@pytest.fixture
def temp_csv_file():
    """Create a temporary CSV file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write('id,amount\n1,100\n2,200\n')
        temp_path = f.name
    yield temp_path
    os.remove(temp_path)


@pytest.fixture
def temp_json_file():
    """Create a temporary JSON file for testing."""
    data = [{"product": "Widget", "price": 9.99}, {"product": "Gadget", "price": 14.99}]
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(data, f)
        temp_path = f.name
    yield temp_path
    os.remove(temp_path)


def test_load_sales_data(temp_csv_file):
    ingestion = DataIngestion()
    df = ingestion.load_sales_data(temp_csv_file)

    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["id", "amount"]
    assert len(df) == 2


def test_load_product_data(temp_json_file):
    ingestion = DataIngestion()
    df = ingestion.load_product_data(temp_json_file)

    assert isinstance(df, pd.DataFrame)
    assert "product" in df.columns
    assert "price" in df.columns
    assert len(df) == 2


def test_file_not_found_error():
    ingestion = DataIngestion()
    with pytest.raises(FileNotFoundError):
        ingestion.load_sales_data('non_existing_file.csv')


def test_empty_file_error():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        temp_path = f.name  # Create an empty file

    ingestion = DataIngestion()
    try:
        with pytest.raises(ValueError):
            ingestion.load_sales_data(temp_path)
    finally:
        os.remove(temp_path)
