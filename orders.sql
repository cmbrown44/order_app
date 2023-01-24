CREATE TABLE IF NOT EXISTS orders (
    NTEGER PRIMARY KEY AUTOINCREMENT, 
    customer_name VARCHAR(30) NOT NULL, 
    drink_size VARCHAR(20) NOT NULL,
    extras VARCHAR(50) NOT NULL,
    price NUMERIC NOT NULL 
);

INSERT INTO orders (customer_name, drink_size, extras, price) VALUES ('Charlie', 'Large', 'Chocolate srpinkles', 3.85);
INSERT INTO orders (customer_name, drink_size, extras, price) VALUES ('Craig', 'Large', 'Sugar', 3.50);
INSERT INTO orders (customer_name, drink_size, extras, price) VALUES ('Louise', 'Medium', 'Cream', 3.25);