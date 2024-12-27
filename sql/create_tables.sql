USE retail_data;

-- Drop tables if they exist
DROP TABLE IF EXISTS sales_table;
DROP TABLE IF EXISTS store_table;
DROP TABLE IF EXISTS product_table;
-- Create table for sales_data
CREATE TABLE sales_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    sale_date DATE,
    quantity INT,
    total_amount DECIMAL(10, 2)
);

-- Create table for store_data
CREATE TABLE store_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100)
);

-- Create table for product_data
CREATE TABLE product_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255),
    price DECIMAL(10, 2),
    stock_quantity INT
);
