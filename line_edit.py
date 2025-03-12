import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 440, 440) # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using line edits")
        self.UI()

    def UI(self):
        self.name_text_box = QLineEdit(self)
        self.name_text_box.setPlaceholderText("Please enter your name")
        self.name_text_box.move(120, 50)
        self.name_text_box.resize(200, 20)

        self.pass_text_box = QLineEdit(self)
        self.pass_text_box.setPlaceholderText("Please enter your password")
        self.pass_text_box.setEchoMode(QLineEdit.Password)
        self.pass_text_box.move(120, 80)
        self.pass_text_box.resize(200, 20)

        button = QPushButton("Save", self)
        button.move(170, 120)
        button.clicked.connect(self.get_values)

        self.show()

    def get_values(self):
        name = self.name_text_box.text()
        password = self.pass_text_box.text()

        self.setWindowTitle("Your name is: " + name + " Your password is: " + password)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()