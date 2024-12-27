import mysql.connector
import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from tests.test_db_connection import connection;

cursor = connection.cursor()

# Function to display the content of a table
def showcase_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
    rows = cursor.fetchall()
    print(f"Data from {table_name}:")
    for row in rows:
        print(row)
    print("\n")

# Showcase the data from each table
showcase_table("sales_table")   # Showcase sales data
showcase_table("store_table") # Showcase customer data
showcase_table("product_table")  # Showcase product data

# Close the connection
cursor.close()
