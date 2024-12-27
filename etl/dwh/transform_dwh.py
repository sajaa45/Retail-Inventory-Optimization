import pandas as pd

def transform(store_data, sales_data, product_data):
    # Transform store data to fit the store_dim table
    store_dim = store_data[['id', 'name', 'address', 'city', 'country']]

    # Transform product data to fit the product_dim table
    product_dim = product_data[['id', 'product name', 'category', 'description', 'brand', 'color', 'size']]

    # Transform sales data to fit the sales_fact table
    sales_fact = sales_data[['id', 'store', 'date', 'product', 'weekly_sales', 'inventory level', 'temperature', 'past promotion of product in lac', 'demand forecast']]
    
    # Convert 'date' to datetime with the correct format
    sales_data['date'] = pd.to_datetime(sales_data['date'], format='%d-%m-%Y', dayfirst=True)

    # Extract unique dates
    unique_dates = sales_data['date'].unique()

    # Create a date dimension from the unique dates
    dim_date = pd.DataFrame({
        'date_id': unique_dates,
        'day': [d.day for d in unique_dates],
        'month': [d.month for d in unique_dates],
        'year': [d.year for d in unique_dates],
        'week': [d.isocalendar()[1] for d in unique_dates],  # ISO week number
        'quarter': [((d.month - 1) // 3) + 1 for d in unique_dates]  # Calculate quarter
    })

    return store_dim, product_dim, dim_date, sales_fact