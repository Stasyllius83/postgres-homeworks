"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# connect to db
with psycopg2.connect(host="localhost", database='north', user='postgres', password='12345') as conn:
    with conn.cursor() as cur:
        # read csv
        with open("north_data/employees_data.csv", 'r', encoding="utf-8") as csv_file:
            csv_data: csv.DictReader = csv.DictReader(csv_file)
            csv_data_list = list(csv_data)
            employees_list = []
            i = 0
            for line_dict in csv_data_list:
                line = line_dict.values()
                tuple_line = tuple(line)
                employees_list.insert(i, tuple_line)
                i += 1
        # execute query
        cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", employees_list)
        cur.execute("SELECT * FROM employees")

        rows = cur.fetchall()
        for row in rows:
            print(row)
        # read csv
        with open("north_data/customers_data.csv", 'r', encoding="utf-8") as csv_file:
            csv_data: csv.DictReader = csv.DictReader(csv_file)
            csv_data_list = list(csv_data)
            customers_list = []
            i = 0
            for line_dict in csv_data_list:
                line = line_dict.values()
                tuple_line = tuple(line)
                customers_list.insert(i, tuple_line)
                i += 1
        # execute query
        cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", customers_list)
        cur.execute("SELECT * FROM customers")

        rows = cur.fetchall()
        for row in rows:
            print(row)
        # read csv
        with open("north_data/orders_data.csv", 'r', encoding="utf-8") as csv_file:
            csv_data: csv.DictReader = csv.DictReader(csv_file)
            csv_data_list = list(csv_data)
            orders_list = []
            i = 0
            for line_dict in csv_data_list:
                line = line_dict.values()
                tuple_line = tuple(line)
                orders_list.insert(i, tuple_line)
                i += 1
        # execute query
        cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", orders_list)
        cur.execute("SELECT * FROM orders")

        rows = cur.fetchall()
        for row in rows:
            print(row)

conn.close()
