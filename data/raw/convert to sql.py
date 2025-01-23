import pandas as pd
from sqlalchemy import create_engine

# Load CSV into a pandas DataFrame
df = pd.read_csv(r'C:\Users\LENOVO\Desktop\Junior\Bi & DB\Project - Copy\data\raw\Retail inventory.csv')

# Create an SQLAlchemy engine to connect to MySQL
engine = create_engine('mysql+mysqlconnector://root:{password}@localhost/retail_data')

# Insert data from the DataFrame to the MySQL table
df.to_sql('retail_data', con=engine, if_exists='append', index=False)

# No need to manually commit, as SQLAlchemy handles this
