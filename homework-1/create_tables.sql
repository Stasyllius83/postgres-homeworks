-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name char(15),
	last_name char(15),
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
)

SELECT * FROM employees

CREATE TABLE customers
(
	customer_id char(10) PRIMARY KEY,
	company_name char(50),
	contact_name char(25)
)

SELECT * FROM customers

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(25),
	employee_id int,
	order_date date,
	ship_city char(25)
)

SELECT * FROM orders