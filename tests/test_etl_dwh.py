import sys
import os


# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl.dwh.extract_dwh import extract
from etl.dwh.transform_dwh import transform
from etl.dwh.load_dwh import load

def run_dwh_process():
    print("Starting the Data Warehouse ETL process...")

    # Step 1: Extract data
    print("Extracting data from cleaned tables...")
    store_data, sales_data, product_data = extract()
    print("Data extraction complete.")

    # Step 2: Transform data
    print("Transforming data for dimensions and facts...")
    store_dim, product_dim, dim_date, sales_fact = transform(store_data, sales_data, product_data)
    print("Data transformation complete.")

    # Step 3: Load data into the Data Warehouse
    print("Loading data into the Data Warehouse...")
    load(store_dim, product_dim, dim_date, sales_fact)
    print("Data loading complete.")
    
    
    print("Data Warehouse ETL process completed successfully.")

if __name__ == "__main__":
    run_dwh_process()