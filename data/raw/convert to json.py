import pandas as pd

# Load the CSV file
csv_file_path = r'C:\Users\LENOVO\Desktop\Junior\Bi & DB\Project - Copy\data\raw\Retail inventory.csv'
data = pd.read_csv(csv_file_path)

# Convert the DataFrame to a JSON file
json_file_path = r'C:\Users\LENOVO\Desktop\Junior\Bi & DB\Project - Copy\data\raw\Retail inventory.json'
data.to_json(json_file_path, orient='records', indent=4)

print("CSV file converted to JSON successfully!")
