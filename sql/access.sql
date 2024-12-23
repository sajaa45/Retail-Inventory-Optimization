CREATE USER 'yasmine'@'%' IDENTIFIED BY 'Default1234';
GRANT ALL PRIVILEGES ON *.* TO 'yasmine'@'%';
FLUSH PRIVILEGES;

"""
    to get access:
    1)on terminal:
        mysql -u yasmine -h 192.168.0.18 -p 3306 -p
    2) Enter password: Default1234
    3) connect to the databse:
        use retail_data;
    """