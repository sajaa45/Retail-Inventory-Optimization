# etl/dwh/load_dwh.py
import sys
import os
from sqlalchemy import  text
import logging

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from tests.test_db_connection import engine, test_database_connection  # Ensure this import works now
connection = test_database_connection()
# Configure logging
logging.basicConfig(level=logging.INFO)

def load(store_dim, product_dim, dim_date, sales_fact):
    try:
        
        # Load sales fact
        try:
            sales_fact.to_sql('sales_fact', con=engine, if_exists='replace', index=False)
            logging.info("Sales fact data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading sales_fact data: {e}")

        # Load store dimension
        try:
            store_dim.to_sql('store_dim', con=engine, if_exists='replace', index=False)
            logging.info("Store dimension data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading store_dim data: {e}")

        # Load product dimension
        try:
            product_dim.to_sql('product_dim', con=engine, if_exists='replace', index=False)
            logging.info("Product dimension data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading product_dim data: {e}")

        # Load date dimension
        try:
            dim_date.to_sql('dim_date', con=engine, if_exists='replace', index=False)
            logging.info("Date dimension data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading dim_date data: {e}")

        # Step 4: Creating views
        try:
            with engine.connect() as db_connection:  # Use engine.connect() for creating the connection
                logging.info("Connected to MySQL server.")
                sql_file_path = "sql/create_views.sql"
                
                # Ensure the file exists
                if not os.path.exists(sql_file_path):
                    logging.error(f"SQL file {sql_file_path} does not exist.")
                    return
                
                with open(sql_file_path, 'r') as sql_file:
                    sql_script = sql_file.read()

                # Remove comments and split the SQL script into individual statements
                sql_statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]

        except Exception as e:
            logging.error(f"Error in creating views: {e}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example usage
# load(store_dim, product_dim, dim_date, sales_fact)
