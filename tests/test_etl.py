from etl.extract_data import extract
from etl.transform_data import transform
from etl.load_data import load  # Uncomment when load function is ready

def run_pipeline():
    # Extract, transform, and print Stock Data
    print("Processing Store Data...")
    raw_stock_data = extract("csv")
    clean_stock_data = transform(raw_stock_data)

    # Extract, transform, and print Store Data
    print("\nProcessing Stock Data...")
    raw_store_data = extract("db")
    clean_store_data = transform(raw_store_data)

    # Extract, transform, and print Product Data
    print("\nProcessing Product Data...")
    raw_product_data = extract("json")
    clean_product_data = transform(raw_product_data)

    # Uncomment this line to load the cleaned data into a database
    load(clean_store_data, "store_table")
    load(clean_stock_data, "sales_table")
    load(clean_product_data, "product_table")

if __name__ == "__main__":
    run_pipeline()
