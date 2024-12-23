import mysql.connector

# Establish a connection to your MySQL database
conn = mysql.connector.connect(
    host="192.168.0.18",
    user="yasmine",
    password="Default1234",
    database="retail_data"  
)

cursor = conn.cursor()

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
conn.close()
