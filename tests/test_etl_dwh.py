import sys
import os
import pandas as pd
from tests.test_db_connection import test_database_connection
import re
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def run_dwh_process():
    try:
        connection = test_database_connection()
        # Step 2: Load the datawarehouse table into a Pandas DataFrame
        print("Loading data from the 'datawarehouse' table...")
        query = "SELECT * FROM datawarehouse"
        datawarehouse_df = pd.read_sql(query, connection)
        print(f"Loaded {len(datawarehouse_df)} rows from 'datawarehouse'.")
        # Step 3: Create dimension tables
        # Store Dimension
        store = datawarehouse_df[['store', 'name', 'address', 'city', 'country']].drop_duplicates().reset_index(drop=True)
        print(f"Store Dimension created with {len(store)} rows.")
        # Product Dimension
        product = datawarehouse_df[['product name', 'category', 'description', 'brand', 'color', 'size', 'material']].drop_duplicates().reset_index(drop=True)
        print(f"Product Dimension created with {len(product)} rows.")
        # Time Dimension
        datawarehouse_df['date'] = datawarehouse_df['date'].apply(
            lambda x: re.sub(r'(\d{1,2})-(\d{1,2})-(\d{4})', r'\1/\2/\3', x)
        )
        datee = pd.to_datetime(datawarehouse_df['date'], errors='coerce', dayfirst=True)
        datawarehouse_df['date'] = datee.dt.date
        time = datawarehouse_df[['date']].copy()
        time['year'] = datee.dt.year
        time['month'] = datee.dt.month
        time['day'] = datee.dt.day
        time = time.drop_duplicates().reset_index(drop=True)
        print(f"Time Dimension created with {len(time)} rows.")
        # Step 4: Create fact table
        sales_fact = datawarehouse_df[['id', 'store', 'date', 'product name', 'weekly_sales','inventory level', 'temperature', 'past promotion of product in lac', 'demand forecast']].drop_duplicates().reset_index(drop=True)
        print(f"Sales Fact table created with {len(sales_fact)} rows.")
        # Step 5: Load fact and dimension tables into the database
        print("Loading dimension and fact tables into the database...")
        store.to_sql('store', con=connection, if_exists='replace', index=False)
        product.to_sql('product', con=connection, if_exists='replace', index=False)
        time.to_sql('time', con=connection, if_exists='replace', index=False)
        sales_fact.to_sql('sales_fact', con=connection, if_exists='replace', index=False)
        connection.commit()
        print("Process completed successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    run_dwh_process()