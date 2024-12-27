from sqlalchemy import create_engine, text

# Define engine at the module level
engine = create_engine('mysql+mysqlconnector://root:Gilmore2003*@localhost/retail_data')

def test_database_connection():
    try:
        # Establish a new connection
        connection = engine.connect()
        print("Connection successful!")
        
        # Read SQL file
        sql_file_path = 'data/raw/store.sql'
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        # Execute SQL script
        for statement in sql_script.split(';'):
            statement = statement.strip()
            
            if statement:  
                try:
                    # If it's a DDL statement (CREATE/DROP), execute it directly
                    if statement.upper().startswith(('CREATE', 'DROP', 'ALTER')):
                        connection.execute(text(statement))
                    else:
                        connection.execute(text(statement))  # For DML (INSERT, SELECT)
                    
                    # If the statement is a SELECT query, fetch and print results
                    if statement.upper().startswith('SELECT'):
                        result = connection.execute(text(statement))
                        for row in result:
                            print(row)
                    
                except Exception as e:
                    print(f"Error executing statement: {statement}\nError: {e}")

        # Commit the changes (if any)
        connection.commit()
        
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
