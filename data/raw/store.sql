CREATE DATABASE retail_data;
USE retail_data;

CREATE TABLE store (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100)
);
insert into store (id, name, Address, City, Country) 
values (1, 'CandleLight & Co.', '3 Eagle Crest Hill', 'Kampot', 'Cambodia'); -- Store selling home goods, like candles and cutting boards

insert into store (id, name, Address, City, Country) 
values (2, 'The Living Essentials', '35 Namekagon Trail', 'Phnom Penh', 'Cambodia'); -- A store in the capital selling lifestyle products, like coconut oil and pillows

insert into store (id, name, Address, City, Country) 
values (3, 'TravelPro Gear', '24996 Village Plaza', 'Siem Reap', 'Cambodia'); -- A store near tourist areas selling travel accessories, like leather bags and water bottles

insert into store (id, name, Address, City, Country) 
values (4, 'Sihanouk Wellness', '9541 Warner Point', 'Sihanoukville', 'Cambodia'); -- A store on the coast selling wellness products, like essential oils and aromatherapy diffusers

insert into store (id, name, Address, City, Country) 
values (5, 'FitGear Hub', '2828 Grover Park', 'Battambang', 'Cambodia'); -- A store in a quieter area selling fitness accessories, like resistance bands
select * from store;