"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
from setting import CUSTOMERS, EMPLOYEES, ORDERS
import psycopg2


def reader_csv(path):
    result = []
    with open(path, 'r', encoding="utf-8") as csvfile:
        reader: csv.DictReader = csv.DictReader(csvfile)
        for row_r in reader:
            result.append(row_r)
    return result


rcsv_c = reader_csv(CUSTOMERS)
rcsv_e = reader_csv(EMPLOYEES)
rcsv_o = reader_csv(ORDERS)

sql_insert_customers = """INSERT INTO customers (customer_id, company_name, contact_name)
    VALUES (%s, %s, %s);"""
sql_insert_employees = """INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes)
    VALUES (%s, %s, %s, %s, %s, %s);"""
sql_insert_orders = """INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)
    VALUES (%s, %s, %s, %s, %s);"""

data_csv_c = ("customer_id", "company_name", "contact_name")
data_csv_e = ("employee_id", "first_name", "last_name", "title", "birth_date", "notes")
data_csv_o = ("order_id", "customer_id", "employee_id", "order_date", "ship_city")

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password='5080')

try:
    with conn:
        with conn.cursor() as cur:
            print("customers")
            for row in rcsv_c:
                data_csv = (row["customer_id"], row["company_name"], row["contact_name"])
                cur.execute(sql_insert_customers, data_csv)
            cur.execute("SELECT * FROM customers ")
            rows = cur.fetchall()
            for rowq in rows:
                print(rowq)

            print("employees")
            for row in rcsv_e:
                data_csv = (row["employee_id"], row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"])
                cur.execute(sql_insert_employees, data_csv)
            cur.execute("SELECT * FROM employees ")
            rows = cur.fetchall()
            for rowq in rows:
                print(rowq)

            print("orders")
            for row in rcsv_o:
                data_csv = (row["order_id"], row["customer_id"], row["employee_id"], row["order_date"], row["ship_city"])
                cur.execute(sql_insert_orders, data_csv)
            cur.execute("SELECT * FROM orders ")
            rows = cur.fetchall()
            for rowq in rows:
                print(rowq)
finally:
    conn.close()
