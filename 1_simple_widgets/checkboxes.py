import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap # needed to display images

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500) # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using checkboxes")
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.surname = QLineEdit(self)
        self.remember = QCheckBox("Remember me", self)
        button = QPushButton("Submit", self)

        self.name.setPlaceholderText("Enter your name")
        self.surname.setPlaceholderText("Enter your surname")

        self.name.move(150, 50)
        self.surname.move(150, 80)
        self.remember.move(150, 110)
        button.move(200, 140)

        button.clicked.connect(self.submit)

        self.show()

    def submit(self):
        if self.remember.isChecked():
            print("Name: " + self.name.text() + "\nSurname: " + self.surname.text() + "\nRemember me checked")
        else:
            print("Name: " + self.name.text() + "\nSurname: " + self.surname.text() + "\nRemember me not checked")



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()