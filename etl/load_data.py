from sqlalchemy import create_engine

def load(clean_data, table_name):
    # Replace with your actual database connection details
    engine = create_engine("mysql+pymysql://yasmine:Default1234@192.168.0.18/retail_data")
    clean_data.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print(f"Data loaded successfully into {table_name}.")