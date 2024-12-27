# etl/dwh/load_dwh.py
import sys
import os
import pandas as pd

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from tests.test_db_connection import engine, test_database_connection  # Ensure this import works now
connection = test_database_connection()

def extract():

    # Extract data from cleaned tables
    store_data = pd.read_sql("SELECT * FROM store_table", con=engine)
    sales_data = pd.read_sql("SELECT * FROM sales_table", con=engine)
    product_data = pd.read_sql("SELECT * FROM product_table", con=engine)

    return store_data, sales_data, product_data
