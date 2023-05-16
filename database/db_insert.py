import sqlite3 as sql
from parser import config_parser


def register_new_item(product_name, client_name, quantity, price_per_unit, total_price,
                      date, data_submitted_by):
    connection = sql.connect(config_parser.db_hostname)
    connection_cursor = connection.cursor()
    connection_cursor.execute("INSERT INTO ss_records (product_name, client_name, quantity, "
                              "price_per_unit, total_price, date, data_submitted_by) "
                              "VALUES (?,?,?,?,?,?,?)",
                              (product_name, client_name, quantity, price_per_unit,
                               total_price, date, data_submitted_by))
    connection.commit()
    connection.close()
    print("New item registered successfully.")