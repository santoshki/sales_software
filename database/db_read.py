import sqlite3 as sql
from parser import config_parser


def read_data(table_name):
    try:
        con = sql.connect(config_parser.db_hostname)
        cur = con.cursor()
        read_query = "SELECT * FROM " + table_name
        cur.execute(read_query)
        data = cur.fetchall()
        print(data)
        return data
    except Exception as e:
        print("Exception occurred while trying to read data from the db:", e)


if __name__ == '__main__':
    read_data(config_parser.db_purchase_stock)
