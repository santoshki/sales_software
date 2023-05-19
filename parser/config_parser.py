import yaml
from yaml.loader import SafeLoader
from pathlib import Path


path = Path(__file__).parent / "../database/config.yaml"
with path.open() as file:
    data = yaml.load(file, Loader=SafeLoader)

current_working_directory = Path.cwd()
db_value = data["database"]
db_location = str(current_working_directory)
db_name = db_value["db_name"]
db_secret_key = db_value["db_secret_key"]
db_hostname = db_location + "\\" + db_name
password_reset_value = db_value["password_reset_value"]

db_table_names = db_value["db_table_names"]
db_users = db_table_names["users"]
db_purchase_stock = db_table_names["purchase_stock"]
db_sale_stock = db_table_names["sale_stock"]
db_stock_inventory = db_table_names["stock_inventory"]
db_settings = db_table_names["settings"]
