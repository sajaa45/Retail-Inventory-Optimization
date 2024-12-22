CREATE DATABASE retail_data;
USE retail_data;
CREATE TABLE sales_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    store VARCHAR(50),
    date DATE,
    product VARCHAR(100),
    weekly_sales INT,
    inventory_level INT,
    temperature DECIMAL(5,2),
    past_promotion_lac DECIMAL(10,3),
    demand_forecast DECIMAL(10,3)
);