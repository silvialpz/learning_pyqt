import sys
from operator import truediv

from PyQt5.QtCore import qQNaN
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500) # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using Radio Buttons")
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.move(150, 50)
        self.name.setPlaceholderText("Enter your name")

        self.surname = QLineEdit(self)
        self.surname.move(150, 80)
        self.surname.setPlaceholderText("Enter your surname")

        self.male = QRadioButton("Male", self)
        self.male.move(150, 110)
        self.male.setChecked(True)

        self.female = QRadioButton("Female", self)
        self.female.move(200, 110)

        button = QPushButton("Submit", self)
        button.move(200, 140)
        button.clicked.connect(self.get_values)

        self.show()

    def get_values(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            print("Name: " + name + "\nSurname: " + surname + "\nYou are a male")
        else:
            print("Name: " + name + "\nSurname: " + surname + "\nYou are a female")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()