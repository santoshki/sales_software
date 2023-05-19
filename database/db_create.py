import sqlite3
from parser import config_parser


def create_table(table_name):
    try:
        connection_db = sqlite3.connect(config_parser.db_hostname)
        cursor_obj = connection_db.cursor()
        if table_name == config_parser.db_purchase_stock:
            new_record_query = "CREATE TABLE " + str(table_name) + "(supplier_name VARCHAR(255), vendor_name " \
                                                                  "VARCHAR(255), product_name VARCHAR(255), " \
                                                                   "quantity VARCHAR(255), " \
                                                                  "price_per_unit VARCHAR(255), total_price " \
                                                                  "VARCHAR(255),   date VARCHAR(255), " \
                                                                  "data_submitted_by VARCHAR(255)); "
        elif table_name == config_parser.db_settings:
            new_record_query = "CREATE TABLE " + str(table_name) + "(gst_percentage_value VARCHAR(255)); "

        elif table_name == config_parser.db_sale_stock:
            new_record_query = "CREATE TABLE " + str(table_name) + "(customer_name VARCHAR(255), product_name " \
                                                                  "VARCHAR(255), customer_email VARCHAR(255), " \
                                                                   "customer_contact_number VARCHAR(255), " \
                                                                   "quantity VARCHAR(255), " \
                                                                  "price_per_unit VARCHAR(255), total_price " \
                                                                  "VARCHAR(255),   date VARCHAR(255));"
        elif table_name == config_parser.db_stock_inventory:
            pass
        create_table_query = new_record_query
        cursor_obj.execute(create_table_query)
        print("Table created successfully!")
        cursor_obj.close()
        connection_db.commit()
    except Exception as e:
        print("Exception occurred while creating table in db", e)


if __name__ == '__main__':
    create_table(config_parser.db_sale_stock)