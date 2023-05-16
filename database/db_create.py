import sqlite3
from parser import config_parser


def create_table(table_name):
    try:
        connection_db = sqlite3.connect(config_parser.db_hostname)
        cursor_obj = connection_db.cursor()
        new_issue_query = "CREATE TABLE " + str(table_name) + "(product_name VARCHAR(255), client_name " \
                                                              "VARCHAR(255), quantity VARCHAR(255), " \
                                                              "price_per_unit VARCHAR(255), total_price " \
                                                              "VARCHAR(255),   date VARCHAR(255), " \
                                                              "data_submitted_by VARCHAR(255)); "
        create_table_query = new_issue_query
        cursor_obj.execute(create_table_query)
        print("Table created successfully!")
        cursor_obj.close()
        connection_db.commit()
    except Exception as e:
        print("Exception occurred while creating table in db", e)


if __name__ == '__main__':
    create_table("ss_records")