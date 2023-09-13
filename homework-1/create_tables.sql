CREATE TABLE customers
(
	customer_id VARCHAR PRIMARY KEY,
	company_name VARCHAR NOT NULL,
	contact_name VARCHAR NOT NULL
);

CREATE TABLE employees
(
	employee_id INT PRIMARY KEY,
	first_name VARCHAR NOT NULL,
	last_name VARCHAR NOT NULL,
	title VARCHAR NOT NULL,
	birth_date DATE NOT NULL,
	notes TEXT NOT NULL
);

CREATE TABLE orders
(
	order_id INT PRIMARY KEY,
	customer_id VARCHAR REFERENCES customers(customer_id),
	employee_id INT REFERENCES employees(employee_id),
	order_date DATE NOT NULL,
	ship_city VARCHAR NOT NULL
);

SELECT * FROM customers;
SELECT * FROM employees;
SELECT * FROM orders;