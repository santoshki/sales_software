import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.i = 0
        self.y = 0
        self.btn = []
        self.setMinimumSize(QSize(300, 200))

        pybutton = QPushButton('Create a button', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100, 100)
        pybutton.move(100, 100)

    def clickMethod(self):
        print('Clicked')
        self.btn.append(QPushButton('New Button', self))

        self.btn[-1].move(self.i, self.y)
        self.i = self.i + 50
        self.y = self.y + 50
        self.btn[-1].show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())