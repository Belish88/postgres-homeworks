from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HW1 = Path.joinpath(ROOT, "homework-1")
NORTH_DATA = Path.joinpath(HW1, "north_data")
CUSTOMERS = Path.joinpath(NORTH_DATA, "customers_data.csv")
EMPLOYEES = Path.joinpath(NORTH_DATA, "employees_data.csv")
ORDERS = Path.joinpath(NORTH_DATA, "orders_data.csv")

# print(CUSTOMERS)