import re
from PyQt5 import QtCore, QtGui, QtWidgets


class SearchableListWidget(QtWidgets.QListWidget):
    def __init__(self, items, parent=None):
        super().__init__(parent=parent)

        self.initial_items = items
        self.set_items(items)

        self.search_box = QtWidgets.QLineEdit()
        self.search_box.textChanged.connect(self.filter)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.search_box)
        self.setLayout(layout)

    def filter(self):
        filtered_items = [item for item in self.initial_items
                          if re.search(self.search_box.text().lower(), item.lower())]

        self.set_items(filtered_items)

    def get_items(self):
        return [str(self.item(i).text()) for i in range(0,6)]

    def set_items(self, items):
        self.clear()
        for name in items:
            self.addItem(name)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    test = SearchableListWidget(['a', 'b', 'c'])
    test.show()

    sys.exit(app.exec_())