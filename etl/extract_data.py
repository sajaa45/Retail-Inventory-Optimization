import sys
import os
import pandas as pd
import json

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from tests.test_db_connection import engine, test_database_connection  # Ensure this import works now
connection = test_database_connection()

def extract(source_type):
    if source_type == "csv":
        # Replace with your actual file path
        return pd.read_csv(r'C:\Users\LENOVO\Desktop\Junior\Bi & DB\Project - Copy\data\raw\Retail inventory.csv')
    elif source_type == "sql":
        query = "SELECT * FROM retail_data"
        return pd.read_sql(query, connection)
    elif source_type == "json":
        # Replace with your actual file path
        with open(r"data\raw\Retail inventory.json", "r") as file:
            return pd.DataFrame(json.load(file))
    else:
        raise ValueError(f"Unsupported source type: {source_type}")