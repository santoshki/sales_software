# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\santosh.a.d.kulkarni\PycharmProjects\sales_software_alpha_v1\designs\settings_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 30, 461, 271))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(120, 40, 81, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.reset_db_button = QtWidgets.QPushButton(self.groupBox)
        self.reset_db_button.setGeometry(QtCore.QRect(120, 80, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.reset_db_button.setFont(font)
        self.reset_db_button.setObjectName("reset_db_button")
        self.back_button = QtWidgets.QPushButton(self.groupBox)
        self.back_button.setGeometry(QtCore.QRect(10, 210, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.reset_values_button = QtWidgets.QPushButton(self.groupBox)
        self.reset_values_button.setGeometry(QtCore.QRect(150, 210, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.reset_values_button.setFont(font)
        self.reset_values_button.setObjectName("reset_values_button")
        self.save_button = QtWidgets.QPushButton(self.groupBox)
        self.save_button.setGeometry(QtCore.QRect(310, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "GST %"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "18"))
        self.reset_db_button.setText(_translate("MainWindow", "Reset Database"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.reset_values_button.setText(_translate("MainWindow", "Reset to default values"))
        self.save_button.setText(_translate("MainWindow", "Save"))