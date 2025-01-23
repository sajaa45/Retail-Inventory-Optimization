import pandas as pd
import re

def transform(data):
    """
    Cleans the input data by performing the following operations:
    - Handling missing values
    - Removing duplicates
    - Converting data types
    - Renaming columns (if necessary)

    Parameters:
    data (pd.DataFrame or dict): The DataFrame or dictionary to be cleaned.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    if data is None:
        raise ValueError("Input data is None. Please check the extract function.")

    # Step 1: Convert dictionary to DataFrame if necessary
    if isinstance(data, dict):
        # If it's a single dictionary, wrap it in a list
        data = [data]
    
    # Convert to DataFrame
    data_frame = pd.DataFrame(data)

    # Step 2: Handle missing values
    # Fill missing values with the mean for numerical columns
    for column in data_frame.select_dtypes(include=['float64', 'int64']).columns:
        data_frame[column] = data_frame[column].fillna(data_frame[column].mean())

    # Fill missing values with a placeholder for categorical columns
    for column in data_frame.select_dtypes(include=['object']).columns:
        data_frame[column] = data_frame[column].fillna('Unknown')

    # Step 3: Remove duplicates
    data_frame = data_frame.drop_duplicates()

    # Step 4: Convert data types (example: converting a date column)
    if 'date' in data_frame.columns:
        # Apply regex to standardize date format (e.g., d-m-Y to d/m/Y)
        data_frame['date'] = data_frame['date'].apply(
                lambda x: re.sub(r'(\d{1,2})-(\d{1,2})-(\d{4})', r'\1/\2/\3', str(x))  # Ensure 'x' is a string
            )
        print(data_frame['date'].head())  # Check before and after applying regex

        # Convert 'date' column to datetime format
        data_frame['date'] = pd.to_datetime(data_frame['date'], format='%d/%m/%Y', dayfirst=True, errors='coerce')

    # Step 5: Rename columns (if necessary)
    # Example: Rename columns to lowercase
    data_frame.columns = [col.lower() for col in data_frame.columns]

    return data_frame
