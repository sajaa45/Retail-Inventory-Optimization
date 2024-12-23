import pandas as pd
import pymysql
import json

def extract(source_type):
    if source_type == "csv":
        # Replace with your actual file path
        return pd.read_csv(r'C:\Users\LENOVO\Desktop\Junior\Bi & DB\Project\data\raw\Retail inventory.csv')
    elif source_type == "db":
        # Replace with your actual database connection details
        connection = pymysql.connect(
            host="192.168.0.18",
            user="yasmine",
            password="Default1234",
            database="retail_data"
        )
        #connection_uri = "mysql+pymysql://root:Gilmore2003*@127.0.0.1/retail_data"
        query = "SELECT * FROM store"
        return pd.read_sql(query, connection)
    elif source_type == "json":
        # Replace with your actual file path
        with open(r"data\raw\products_data.json", "r") as file:
            return pd.DataFrame(json.load(file))
    else:
        raise ValueError(f"Unsupported source type: {source_type}")