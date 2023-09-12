-- SQL-команды для создания таблиц
CREATE TABLE employees IF NOT EXISTS
(
	employee_id int PRIMARY KEY,
	first_name char(15),
	last_name char(15),
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
);

CREATE TABLE customers IF NOT EXISTS
(
	customer_id char(10) PRIMARY KEY,
	company_name char(50),
	contact_name char(25)
);

CREATE TABLE orders IF NOT EXISTS
(
	order_id int PRIMARY KEY,
	customer_id char(25) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date,
	ship_city char(25)
);