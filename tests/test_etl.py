import sys
import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from etl.extract_data import extract
from etl.transform_data import transform
from etl.load_data import load 



def run_pipeline(choice):
    try:
        print("Processing Data...")
        raw_data = extract(choice)
        #transform Data
        clean_data = transform(raw_data)
         # Load the cleaned data into the database
        print("\nLoading Cleaned Data into Database...")
        load(clean_data, "datawarehouse")
        print("ETL Pipeline completed successfully.")
        

    except Exception as e:
        print(f"An error occurred during the ETL pipeline execution: {e}")

if __name__ == "__main__":
    run_pipeline()
