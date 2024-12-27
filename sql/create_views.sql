--  View for Daily Sales Summary
CREATE OR REPLACE VIEW mv_daily_sales_summary AS
SELECT 
    STR_TO_DATE(s.date, '%d-%m-%Y') AS sales_date, 
    d.day,
    d.month,
    d.year,
    SUM(s.weekly_sales) AS total_sales,
    COUNT(s.id) AS total_transactions
FROM 
    sales_fact s
JOIN 
    dim_date d ON STR_TO_DATE(s.date, '%d-%m-%Y') = d.date_id 
GROUP BY 
    STR_TO_DATE(s.date, '%d-%m-%Y'),d.day, d.month, d.year;  
DESCRIBE product_dim;
--  View for Monthly Sales by Product
CREATE OR REPLACE VIEW mv_monthly_sales_by_product AS
SELECT 
	d.month,
    d.year,
    p.`product name`
FROM 
    sales_fact s
JOIN 
    product_dim p ON s.product = p.`product name`
JOIN 
    dim_date d ON STR_TO_DATE(s.date, '%d-%m-%Y') = d.date_id;
    select date(date_id) from dim_date;
    SELECT 
    DATE_FORMAT(STR_TO_DATE(date, '%d-%m-%Y'), '%Y-%m-%d') AS date
FROM 
    sales_fact;
    select date from sales_fact;
--  View for Inventory Levels
CREATE OR REPLACE VIEW mv_inventory_levels AS
SELECT 
    p.`product name`,
    SUM(s.`inventory level`) AS total_inventory
FROM 
    sales_fact s
JOIN 
    product_dim p ON s.product = p.`product name`
GROUP BY 
    p.`product name`;