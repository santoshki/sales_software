from datetime import date
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import main
import new_items
import about
import settings
import test
from database import db_insert, db_update
import datetime

from test import MyScrollWidget
from usecase import db_proc
from PyQt5.QtCore import QSize
import purchases
import message_display
import getpass
import sales_new

buttons_add = []


class Main_UI(QtWidgets.QMainWindow, main.Ui_MainWindow):
    """def open_window_purchases(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = purchases.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        today = date.today()
        self.ui.data_submitted_by.setPlainText(str(getpass.getuser()))
        self.ui.current_date.setPlainText(str(today))
        self.ui.save_button.clicked.connect(self.save_purchase_details)
        self.ui.back_button.clicked.connect(self.back_screen)
        self.ui.reset_button.clicked.connect(self.reset_purchase_form)
        self.ui.quantity_spinBox.textChanged.connect(self.text_changed)
        self.ui.price_per_unit_spinBox.textChanged.connect(self.text_changed)

    def text_changed(self):
        quantity = self.ui.quantity_spinBox.value()
        price_per_unit = self.ui.price_per_unit_spinBox.value()
        quantity_int = int(quantity)
        price_per_unit_int = int(price_per_unit)
        total_price = quantity_int * price_per_unit_int
        self.ui.total_price.setPlainText(str(total_price))

    def save_purchase_details(self):
        print("capturing information about new purchases....")
        supplier_name = self.ui.supplier_name.toPlainText()
        vendor_name = self.ui.vendor_name.toPlainText()
        product_name = self.ui.product_name.toPlainText()
        quantity = self.ui.quantity_spinBox.value()
        price_per_unit = self.ui.price_per_unit_spinBox.value()
        total_price = self.ui.total_price.toPlainText()
        date = self.ui.current_date.toPlainText()
        data_submitted_by = self.ui.data_submitted_by.toPlainText()

        print("Supplier Name:", supplier_name)
        print("Product Name:", product_name)
        print("Vendor Name:", vendor_name)
        print("Quantity:", quantity)
        print("Price per unit:", price_per_unit)
        print("Total price:", total_price)
        print("Date:", date)
        print("Data submitted by:", data_submitted_by)
        data_reg = db_insert.register_purchase(supplier_name, product_name, vendor_name, quantity, price_per_unit,
                                               total_price, date, data_submitted_by)
        if data_reg == 1:
            self.window.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = message_display.Ui_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()
            self.ui.label.setText("Purchase details saved successfully!")
            self.ui.okay_button.clicked.connect(self.back_screen)

        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = message_display.Ui_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()
            self.ui.label.setText("!!Error while saving details in db.")
            self.ui.okay_button.clicked.connect(self.back_screen)

    def reset_purchase_form(self):
        self.ui.supplier_name.setPlainText("")
        self.ui.vendor_name.setPlainText("")
        self.ui.product_name.setPlainText("")
        self.ui.quantity_spinBox.setValue(0)
        self.ui.price_per_unit_spinBox.setValue(0)
        self.ui.total_price.setPlainText("")"""

    def open_window_sales(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = sales_new.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.j = 0
        self.item_no_value = 2
        self.window.show()
        myQListWidget = QListWidget()
        """item_text = ['sample 1', 'sample 2']
        self.ui.comboBox.addItems(item_text)
        self.ui.back_button.clicked.connect(self.back_screen)
        self.ui.reset_button.clicked.connect(self.reset_sales_form)"""
        self.ui.plainTextEdit_4.setPlainText("1")
        self.ui.item_no_textfield = QtWidgets.QPlainTextEdit(self.ui.centralwidget)
        self.ui.item_no_textfield.setGeometry(QtCore.QRect(10, (self.j * 10) + 275, 40, 50))
        # self.ui.add_new_row_button.clicked.connect(self.add_new_data)
        ct = MyScrollWidget()
        self.ui.add_new_row_button.clicked.connect(lambda text: self.add_new_data("add"))
        self.ui.spinBox.textChanged.connect(self.get_total_inr)
        self.ui.spinBox_2.textChanged.connect(self.get_total_inr)

    def get_total_inr(self):
        units_sold_qty = self.ui.spinBox.value()
        price_per_unit_qty = self.ui.spinBox_2.value()
        self.ui.plainTextEdit_6.setPlainText(str(units_sold_qty * price_per_unit_qty))

    def add_new_data(self, text):
        try:
            if text == "add":
                print("New Row to be added")

                self.ui.item_no_textfield = QtWidgets.QPlainTextEdit(self.ui.centralwidget)
                self.ui.product_name_dropdown = QtWidgets.QComboBox(self.ui.centralwidget)
                self.ui.vendor_name_textfield = QtWidgets.QPlainTextEdit(self.ui.centralwidget)
                self.ui.units_sold_spinner = QtWidgets.QSpinBox(self.ui.centralwidget)
                self.ui.price_per_unit_spinner = QtWidgets.QSpinBox(self.ui.centralwidget)
                self.ui.total_amount_textfield = QtWidgets.QPlainTextEdit(self.ui.centralwidget)
                self.ui.button_add = QtWidgets.QPushButton(self.ui.centralwidget)
                self.ui.button_remove = QtWidgets.QPushButton(self.ui.centralwidget)
                self.ui.total_amount_textfield = QtWidgets.QPlainTextEdit(self.ui.centralwidget)

                self.ui.item_no_textfield.setGeometry(QtCore.QRect(10, (self.j * 10) + 275, 40, 50))
                self.ui.item_no_textfield.setObjectName("item_no_" + str(self.j))
                self.ui.item_no_textfield.setPlainText(str(self.item_no_value))
                self.item_no_value = self.item_no_value + 1

                self.ui.product_name_dropdown.setGeometry(QtCore.QRect(80, (self.j * 10) + 275, 140, 50))
                self.ui.product_name_dropdown.setObjectName("product_name_dropdown_" + str(self.j))

                self.ui.vendor_name_textfield.setGeometry(QtCore.QRect(250, (self.j * 10) + 275, 120, 50))
                self.ui.vendor_name_textfield.setObjectName("vendor_name_" + str(self.j))

                self.ui.units_sold_spinner.setGeometry(QtCore.QRect(400, (self.j * 10) + 275, 80, 50))
                self.ui.units_sold_spinner.setObjectName("units_sold_" + str(self.j))

                units_sold_qty = self.ui.units_sold_spinner.value()

                self.ui.price_per_unit_spinner.setGeometry(QtCore.QRect(510, (self.j * 10) + 275, 80, 50))
                self.ui.price_per_unit_spinner.setObjectName("price_per_unit_" + str(self.j))
                price_per_unit = self.ui.price_per_unit_spinner.value()
                total_ppu = 0
                total_usp = 0
                self.ui.units_sold_spinner.textChanged.connect(lambda data3: self.add_new_data("spinner"))
                self.ui.price_per_unit_spinner.textChanged.connect(lambda data3: self.add_new_data("spinner"))
                #total_usp = self.ui.units_sold_spinner.textChanged.connect(
                    #lambda text: self.get_total_inr2(self.ui.units_sold_spinner.value(),
                                                     #self.ui.price_per_unit_spinner.value()))

                #total_ppu = self.ui.price_per_unit_spinner.textChanged.connect(
                    #lambda text: self.get_total_inr2(self.ui.units_sold_spinner.value(),
                                                     #self.ui.price_per_unit_spinner.value()))

                self.ui.total_amount_textfield.setGeometry(QtCore.QRect(620, (self.j * 10) + 275, 100, 50))
                self.ui.total_amount_textfield.setObjectName("total_amount_" + str(self.j))
                self.ui.total_amount_textfield.setPlainText(str(total_usp))

                self.ui.button_add.setGeometry(QtCore.QRect(750, (self.j * 10) + 275, 60, 50))
                self.ui.button_add.setObjectName("button_add_" + str(self.j))
                self.ui.button_add.setText("+")
                buttons_add.append(self.ui.button_add.objectName())
                self.ui.button_add.clicked.connect(lambda data: self.add_new_data("add"))
                self.ui.button_remove.setGeometry(QtCore.QRect(830, (self.j * 10) + 275, 60, 50))
                self.ui.button_remove.setObjectName("button_remove_" + str(self.j))
                self.ui.button_remove.setText("-")
                # self.ui.button_remove.clicked.connect(lambda text: self.delete_row(self.ui.button_remove.objectName()))
                # self.ui.button_remove.clicked.connect(self.delete_row)
                self.ui.button_remove.clicked.connect(lambda data2: self.add_new_data("remove"))
                self.ui.item_no_textfield.show()
                self.ui.product_name_dropdown.show()
                self.ui.vendor_name_textfield.show()
                self.ui.units_sold_spinner.show()
                self.ui.price_per_unit_spinner.show()
                self.ui.total_amount_textfield.show()
                self.ui.button_add.show()
                self.ui.button_remove.show()
                self.window.update()
                self.ui.add_new_row_button.setEnabled(False)
                self.j = self.j + 8
                myQListWidget = QListWidget()
                # myQListWidget.addItem(self.ui.item_no_textfield)
                print("button clicked:", self.ui.button_add.objectName())

                print("Buttons added:", buttons_add)
                """for i in buttons_add:
                    if i == "button_add_" + str(row_num-8):
                        if self.ui.button_add.objectName() == i:
                            self.ui.button_add.deleteLater()"""
                """if self.ui.button_add.objectName() == "button_add_" + str(row_num):
                    self.ui.button_add.setEnabled(False)"""
            elif text == "remove":
                print(self.ui.total_amount_textfield.getPaintContext())
                self.ui.total_amount_textfield.deleteLater()

            elif text == "spinner":
                self.ui.total_amount_textfield.setPlainText(str(self.ui.units_sold_spinner.value()*self.ui.price_per_unit_spinner.value()))
        except Exception as e:
            print(e)

    def get_total_inr2(self, units_sold_qty, price_per_unit):

        total_inr = units_sold_qty * price_per_unit
        self.findChild(QPlainTextEdit)

        print(total_inr)
        return total_inr

    def delete_row(self):
        import main3
        import wx
        app = wx.App()
        frame = main3.MyFrame()
        app.MainLoop()

    def reset_sales_form(self):
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.customer_name.setPlainText(" ")
        self.ui.quantity_spinBox.setValue(0)
        self.ui.price_per_unit_spinBox.setValue(0)
        self.ui.total_price.setPlainText(" ")

    def open_window_settings_app(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = settings.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        gst_percentage_value = db_proc.db_get_values()
        self.ui.gst_percentage_value.setPlainText(str(gst_percentage_value))
        self.ui.back_button.clicked.connect(self.back_screen)
        self.ui.save_button.clicked.connect(self.save_settings)
        self.ui.reset_values_button.clicked.connect(self.reset_settings)

    def reset_settings(self):
        print("Resetting settings to default values...")
        db_update.db_update_table("18")
        self.ui.gst_percentage_value.setPlainText("18")

    def save_settings(self):
        db_update.db_update_table(self.ui.gst_percentage_value.toPlainText())
        print("New GST% value =", self.ui.gst_percentage_value.toPlainText())

    def open_window_about_app(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = about.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.okay_button.clicked.connect(self.app_about_okay)

    def app_about_okay(self):
        self.window.close()

    def open_window_new_items(self):
        self.window = QtWidgets.QMainWindow()
        layout = QtWidgets.QVBoxLayout()
        self.ui = new_items.New_ItemsWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.save_button.clicked.connect(self.save_new_items)
        self.ui.back_button.clicked.connect(self.back_screen)
        self.ui.reset_button.clicked.connect(self.reset_form)

    def __init__(self, parent=None):
        super(Main_UI, self).__init__(parent)
        self.setupUi(self)
        self.new_items_button.clicked.connect(self.open_window_new_items)
        self.sales_button.clicked.connect(self.open_window_sales)
        self.settings_button.clicked.connect(self.open_window_settings_app)
        self.about_button.clicked.connect(self.open_window_about_app)
        self.exit_button.clicked.connect(self.app_exit)
        self.refresh_button.clicked.connect(self.refresh_data)

    def refresh_data(self):
        for i in range(101):
            time.sleep(0.05)
            self.progressBar.setValue(i)
        self.progressBar.setValue(0)

    def app_exit(self):
        print("Exiting the application")
        sys.exit()

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
        # date = self.ui.dateTimeEdit.textFromDateTime()
        self.ui.total_price.setPlainText(str(total_price))
        print("Product Name:", product_name)
        print("Client Name:", client_name)
        print("Quantity:", quantity)
        print("Price per unit:", price_per_unit)
        print("Total price:", total_price)
        print("Date:", date)
        print("Data submitted by:", data_submitted_by)
        db_insert.register_purchase(product_name, client_name, quantity, price_per_unit, total_price, date,
                                    data_submitted_by)

    def back_screen(self):
        self.window.close()

    def reset_form(self):
        self.ui.product_name.setPlainText(" ")
        self.ui.client_name.setPlainText(" ")
        self.ui.quantity.setPlainText(" ")
        self.ui.per_unit_price.setPlainText(" ")
        self.ui.total_price.setPlainText(" ")


def main():
    app = QApplication(sys.argv)
    form = Main_UI()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
