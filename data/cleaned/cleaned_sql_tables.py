import sys
import os
from sqlalchemy import text

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from tests.test_db_connection import test_database_connection

# Establish connection to the database
connection = test_database_connection()

# Check if the connection is valid
if connection:
    # Function to display the content of a table
    def showcase_table(table_name):
        # Use the connection to execute the query with text() for SQLAlchemy compatibility
        result = connection.execute(text(f"SELECT * FROM {table_name} LIMIT 5"))
        
        print(f"Data from {table_name}:")
        for row in result:
            print(row)
        print("\n")
    
    # Showcase the data from each table
    showcase_table("sales_fact")   # Showcase sales data
    showcase_table("store")   # Showcase customer data
    showcase_table("product")  # Showcase product data

    # Close the connection
    connection.close()  # Close the connection properly
else:
    print("Failed to establish a database connection.")
