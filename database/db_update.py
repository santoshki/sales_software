import sqlite3 as sql
from parser import config_parser


def db_delete_table(table_name):
    try:
        connection = sql.connect(config_parser.db_hostname)
        query = "DROP TABLE " + str(table_name)
        connection.execute(query)
        print("Table dropped from the db.")
        connection.commit()
        connection.close()
    except Exception as e:
        print("Exception occurred while dropping the table in the db", e)


def db_update_table(gst_percentage_value):
    try:
        connection = sql.connect(config_parser.db_hostname)
        connection.execute("UPDATE ss_settings SET gst_percentage_value = ?", (gst_percentage_value,))
        print("Table values updated in db.")
        connection.commit()
        connection.close()

    except Exception as e:
        print("Exception occurred while updating value in db", e)


if __name__ == '__main__':
   #db_update_table("19")
   db_delete_table(config_parser.db_settings)
