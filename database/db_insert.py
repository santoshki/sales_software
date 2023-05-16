import sqlite3 as sql
from parser import config_parser


def register_new_item(product_name, client_name, quantity, price_per_unit, total_price,
                      date, data_submitted_by):
    try:
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
    except Exception as e:
        print("Exception occurred while registering new item in the database:", e)


def insert_values(gst_percentage_value):
    try:
        connection = sql.connect(config_parser.db_hostname)
        connection_cursor = connection.cursor()
        connection_cursor.execute("INSERT INTO ss_settings (gst_percentage_value) "
                                  "VALUES (?)", (gst_percentage_value,))
        connection.commit()
        connection.close()
        print("Data inserted successfully")
    except Exception as e:
        print("Exception occurred while inserting values into database:", e)


if __name__ == '__main__':
    insert_values("18")
