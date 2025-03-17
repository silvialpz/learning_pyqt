import sys

from PyQt5.QtCore import qQNaN
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500) # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using comboboxes")
        self.UI()

    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 100)

        button = QPushButton("Save", self)
        button.move(150, 130)
        button.clicked.connect(self.get_value)

        # using methods to add items
        self.combo.addItem("Python")
        self.combo.addItems(["C", "C#", "PHP"])

        # using for loop to add items
        list1 = ["batman", "superman", "spiderman"]
        for name in list1:
            self.combo.addItem(name)

        for number in range(80, 101):
            self.combo.addItem(str(number))

        self.show()

    def get_value(self):
        value = self.combo.currentText()
        print(value)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()