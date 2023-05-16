from database import db_read
from parser import config_parser


def db_get_values():
    data = db_read.read_data(config_parser.db_settings)
    return data[0]

if __name__ == '__main__':
   value = db_get_values()
   print(value)