import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350) # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using labels")
        self.UI()

    def UI(self):
        self.text = QLabel("My Text", self) # When you create a label you also create a fixed size
        enter_button = QPushButton("Enter", self)
        exit_button = QPushButton("Exit", self)

        self.text.move(150, 50)
        enter_button.move(100, 80)
        exit_button.move(200, 80)

        enter_button.clicked.connect(self.enter_func)
        exit_button.clicked.connect(self.exit_func)
        self.show()

    def enter_func(self):
        self.text.setText("You clicked Enter")
        self.text.resize(150, 20)

    def exit_func(self):
        self.text.setText("You clicked Exit")
        self.text.resize(150, 20)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()