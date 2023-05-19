import sqlite3 as sql
from parser import config_parser


def register_purchase(supplier_name, product_name, vendor_name, quantity, price_per_unit, total_price,
                      date, data_submitted_by):
    try:
        connection = sql.connect(config_parser.db_hostname)
        connection_cursor = connection.cursor()
        connection_cursor.execute("INSERT INTO purchase_stock (supplier_name, product_name, vendor_name, quantity, "
                                  "price_per_unit, total_price, date, data_submitted_by) "
                                  "VALUES (?,?,?,?,?,?,?,?)",
                                  (supplier_name, product_name, vendor_name, quantity, price_per_unit, total_price,
                                   date, data_submitted_by))
        connection.commit()
        connection.close()
        print("New Purchase registered successfully.")
        return 1
    except Exception as e:
        print("Exception occurred while registering new item in the database:", e)
        return 0


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
