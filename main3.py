"""from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QLabel, QPlainTextEdit


class NewWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__(parent)
        self.label = QLabel('New Window!')
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.layout = QGridLayout(centralWidget)
        self.layout.addWidget(self.label)


class MyWindow(QtWidgets.QMainWindow, QPushButton):
    def __init__(self):
        super(MyWindow, self).__init__()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.setWindowTitle("ASSET")
        self.setGeometry(QtCore.QRect(10, 300, 600, 600))
        self.Button = QPushButton('Action', self)
        self.Button.setGeometry(QtCore.QRect(10, 100, 75, 75))
        self.Button.setObjectName("Test Action")
        self.Button.clicked.connect(self.Action)
        self.textfield = QPlainTextEdit()
        self.textfield2 = QPlainTextEdit()
        self.layout = QGridLayout(centralWidget)
        self.layout.addWidget(self.Button)

        self.new_window = NewWindow(self)

    def Action(self):
        print("Adding new elements....")

        self.textfield.setGeometry(QtCore.QRect(10, 200, 50, 50))
        self.layout.addWidget(self.textfield)
        self.textfield2.setGeometry(QtCore.QRect(10, 400, 50, 50))
        self.layout.addWidget(self.textfield2)
        self.layout = QGridLayout(centralWidget)
        self.new_window.textfield = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.new_window.textfield.setGeometry(10, 300, 75, 50)
        self.new_window.textfield.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
"""

import wx


class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='New Sales window')

        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)
        self.number_of_buttons = 0
        self.number_of_txt_fields = 0
        self.panel = wx.Panel(self)
        self.i = 0
        self.my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.frame = wx.Frame()

        #self.text_ctrl = wx.TextCtrl(self.panel)

        my_btn_remove = wx.Button(self.panel, label='Remove Textbox')
        my_btn_add = wx.Button(self.panel, label='Add Textbox')
        my_btn_add.Bind(wx.EVT_BUTTON, self.on_click)
        my_btn_remove.Bind(wx.EVT_BUTTON, self.on_press)
        self.my_sizer.Add(my_btn_add, 0, wx.ALL | wx.CENTER, 5)
        self.my_sizer.Add(my_btn_remove, 0, wx.ALL | wx.CENTER, 5)

        self.panel.SetSizer(self.my_sizer)

        self.Show()

    def on_press(self, event):
        print("Total number of buttons present:", self.number_of_buttons)
        sizer_item_button = self.my_sizer.GetItem(self.number_of_buttons-1)
        #sizer_txt_field = self.my_sizer.GetItem(self.number_of_txt_fields - 1)
        widget_button = sizer_item_button.GetWindow()
        #widget_text_field = sizer_txt_field.GetWindow()

        self.my_sizer.Hide(widget_button)
        #self.my_sizer.Hide(widget_text_field)
        widget_button.Destroy()
        print("Button removed")
        #widget_text_field.Destroy()
        self.number_of_buttons -= 1
        self.number_of_txt_fields -= 1
        """self.frame..Layout()
        self.frame.Fit()"""
        print("Text box removed")
        """value = self.text_ctrl.GetValue()

        if not value:

            print("You didn't enter anything!")

        else:

            print(f'You typed: "{value}"')"""

    def on_click(self, event):
        self.text_ctrl = wx.TextCtrl(self.panel, pos=(5, (self.i*1 + 5)))
        print("Text box added")
        my_btn_new_row = wx.Button(self.panel, label='add new row', pos=(225, self.i+5), size=(80, 25))

        self.my_sizer.Add(my_btn_new_row, 0, wx.ALL | wx.CENTER, 5)
        print("Button added")
        self.number_of_buttons += 1
        print("Total number of buttons added:", self.number_of_buttons)
        self.panel.SetSizer(self.my_sizer)
        self.Show()
        self.i = self.i + 30


if __name__ == '__main__':
    app = wx.App()

    frame = MyFrame()

    app.MainLoop()
