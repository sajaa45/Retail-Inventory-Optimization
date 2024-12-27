import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from tests.test_db_connection import engine 

def load(clean_data, table_name):
    clean_data['id'] = range(1, len(clean_data) + 1)
    # Reorder the columns to make 'id' the first column
    cols = ['id'] + [col for col in clean_data.columns if col != 'id']
    clean_data = clean_data[cols]
    clean_data.to_sql(table_name, con=engine, if_exists="replace", index=False)
    
    print(f"Data loaded successfully into {table_name}.")