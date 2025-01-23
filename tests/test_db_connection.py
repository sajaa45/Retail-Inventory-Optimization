from sqlalchemy import create_engine
import os

# Define engine at the module level
password = os.getenv("SQL_PASSWORD")
if password is None:
    print("SQL_PASSWORD environment variable is not set.")

engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost/retail_data')

def test_database_connection():
    try:
        # Establish a new connection
        connection = engine.connect()
        print("Connection established successfully.")
        return connection

    except Exception as e:
        print(f"Connection failed: {e}")
        return None

# Run the test if executed directly
if __name__ == "__main__":
    connection = test_database_connection()
    if connection:
        print("Database connection test passed.")
    else:
        print("Database connection test failed.")
