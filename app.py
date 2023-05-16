from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import main
import new_items
from database import db_insert
import datetime

class Main_UI(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def open_window_new_items(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = new_items.New_ItemsWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.save_button.clicked.connect(self.save_new_items)
        self.ui.back_button.clicked.connect(self.back_home_screen)
        self.ui.reset_button.clicked.connect(self.reset_form)

    def __init__(self, parent=None):
        super(Main_UI, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_window_new_items)
        self.pushButton_3.clicked.connect(self.clicked)

    def clicked(self):
        print("Settings button pressed.")
        print(self.textEdit.toPlainText())

    def save_new_items(self):
        print("capturing information about new items for registration....")
        product_name = self.ui.product_name.toPlainText()
        client_name = self.ui.client_name.toPlainText()
        quantity = self.ui.quantity.toPlainText()
        price_per_unit = self.ui.per_unit_price.toPlainText()
        quantity_int = int(quantity)
        price_per_unit_int = int(price_per_unit)
        self.ui.per_unit_price.textChanged.connect(self.text_changed)
        total_price = quantity_int * price_per_unit_int
        data_submitted_by = self.ui.data_submitted_by.toPlainText()
        date = datetime.datetime.now()
        #date = self.ui.dateTimeEdit.textFromDateTime()
        self.ui.total_price.setPlainText(str(total_price))
        print("Product Name:", product_name)
        print("Client Name:", client_name)
        print("Quantity:", quantity)
        print("Price per unit:", price_per_unit)
        print("Total price:", total_price)
        print("Date:", date)
        print("Data submitted by:", data_submitted_by)
        db_insert.register_new_item(product_name, client_name, quantity, price_per_unit, total_price, date, data_submitted_by)

    def back_home_screen(self):
        self.window.close()

    def reset_form(self):
        self.ui.product_name.setPlainText(" ")
        self.ui.client_name.setPlainText(" ")
        self.ui.quantity.setPlainText(" ")
        self.ui.per_unit_price.setPlainText(" ")
        self.ui.total_price.setPlainText(" ")

    def text_changed(self):
        print("Text change detected")

def main():
    app = QApplication(sys.argv)
    form = Main_UI()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
