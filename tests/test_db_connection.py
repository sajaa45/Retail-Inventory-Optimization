import pymysql

def test_database_connection():
    try:
        connection = pymysql.connect(
            host="192.168.0.18",  # Replace with your MySQL server's IP
            user="yasmine",       # Your MySQL username
            password="Default1234",  # Your MySQL password
            database="retail_data",  # Your database name
            port=3306              # MySQL port (default: 3306)
        )
        print("Connection successful!")
        return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

# Run the test if executed directly
if __name__ == "__main__":
    success = test_database_connection()
    if success:
        print("Database connection test passed.")
    else:
        print("Database connection test failed.")
