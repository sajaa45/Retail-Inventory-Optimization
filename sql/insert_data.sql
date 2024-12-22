LOAD DATA LOCAL INFILE 'C:\Users\LENOVO\Desktop\Junior\Bi & DB\Project\data\raw\Retail inventory for database.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
select * from sales_data;