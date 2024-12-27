-- CREATE DATABASE retail_data;
-- USE retail_data;

DROP TABLE IF EXISTS store;

CREATE TABLE store (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100)
);

-- Insert values without explicitly specifying the 'id' column
INSERT INTO store (name, address, city, country) 
VALUES ('CandleLight & Co.', '3 Eagle Crest Hill', 'Kampot', 'Cambodia'), -- Store selling home goods, like candles and cutting boards
       ('The Living Essentials', '35 Namekagon Trail', 'Phnom Penh', 'Cambodia'), -- A store in the capital selling lifestyle products, like coconut oil and pillows
       ('TravelPro Gear', '24996 Village Plaza', 'Siem Reap', 'Cambodia'), -- A store near tourist areas selling travel accessories, like leather bags and water bottles
       ('Sihanouk Wellness', '9541 Warner Point', 'Sihanoukville', 'Cambodia'), -- A store on the coast selling wellness products, like essential oils and aromatherapy diffusers
       ('FitGear Hub', '2828 Grover Park', 'Battambang', 'Cambodia'); -- A store in a quieter area selling fitness accessories, like resistance bands

-- Fetch all rows from the table
SELECT * FROM store;
