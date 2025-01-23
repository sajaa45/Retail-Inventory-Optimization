import sys
import os
import csv
from sqlalchemy import text

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from tests.test_db_connection import test_database_connection

# Establish connection to the database
connection = test_database_connection()

# Check if the connection is valid
if connection:
    # Function to export table content to CSV
    def export_table_to_csv(table_name, filename):
        # Use the connection to execute the query with text() for SQLAlchemy compatibility
        result = connection.execute(text(f"SELECT * FROM {table_name}"))
        
        # Fetch column names
        columns = result.keys()
        
        # Open a CSV file to write the data
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Write the header (column names)
            writer.writerow(columns)
            
            # Write all rows
            for row in result:
                writer.writerow(row)
        
        print(f"Data from {table_name} has been written to {filename}")

    # Export data from each table to CSV
    export_table_to_csv("sales_fact", "sales_fact.csv")  # Export sales data
    export_table_to_csv("store", "store.csv")  # Export customer data
    export_table_to_csv("product", "product.csv")  # Export product data

    # Close the connection
    connection.close()  # Close the connection properly
else:
    print("Failed to establish a database connection.")
