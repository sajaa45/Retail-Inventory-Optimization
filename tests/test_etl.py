import sys
import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from etl.extract_data import extract
from etl.transform_data import transform
from etl.load_data import load 



def run_pipeline():
    try:
        
        # Extract, transform, and print Store Data
        print("Processing Store Data...")
        raw_stock_data = extract("csv")
        clean_stock_data = transform(raw_stock_data)
        
        # Extract, transform, and print Stock Data
        print("\nProcessing Stock Data...")
        raw_store_data = extract("db")
        clean_store_data = transform(raw_store_data)

        # Extract, transform, and print Product Data
        print("\nProcessing Product Data...")
        raw_product_data = extract("json")
        clean_product_data = transform(raw_product_data)

        # Load the cleaned data into the database
        print("\nLoading Cleaned Data into Database...")
        load(clean_store_data, "store_table")
        load(clean_stock_data, "sales_table")
        load(clean_product_data, "product_table")
        
        print("ETL Pipeline completed successfully.")

    except Exception as e:
        print(f"An error occurred during the ETL pipeline execution: {e}")

if __name__ == "__main__":
    run_pipeline()
