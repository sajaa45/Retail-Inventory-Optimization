-- Dimension Table: Store
CREATE TABLE store_dim (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100)
);

-- Dimension Table: Product
CREATE TABLE product_dim (
    id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255),
    price DECIMAL(10, 2),
    stock_quantity INT
);

-- Dimension Table: Date
CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    day INT,
    month INT,
    year INT,
    week INT,
    quarter INT
);

-- Fact Table: Sales
CREATE TABLE sales_fact (
    id INT AUTO_INCREMENT PRIMARY KEY,
    store_id INT,
    product_id INT,
    sale_date DATE,
    quantity INT,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (store_id) REFERENCES store_dim(id),
    FOREIGN KEY (product_id) REFERENCES product_dim(id),
    FOREIGN KEY (sale_date) REFERENCES dim_date(date_id)
);