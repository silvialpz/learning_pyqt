import sysxs
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont  # This is how you can use fonts

font = QFont("Times New Roman", 16)  # (font family, font size)
                                     # Check available fonts in Font Book

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)  # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using Spin Boxes")
        self.UI()

    def UI(self):
        self.spinbox = QSpinBox(self)
        self.spinbox.move(150, 100)
        self.spinbox.setFont(font)

        # self.spinbox.setMinimum(25)  # default min, max values are 0, 99
        # self.spinbox.setMaximum(110)

        self.spinbox.setRange(25, 110)

        # To add symbols
        # self.spinbox.setPrefix("$ ")
        self.spinbox.setSuffix(" cm")

        # Modify the step size
        self.spinbox.setSingleStep(5)

        # Do something when value is changed
        # self.spinbox.valueChanged.connect(self.get_value)

        # Do something with a button
        button = QPushButton("Send", self)
        button.move(150, 140)
        button.clicked.connect(self.get_value)

        self.show()

    def get_value(self):
        value = self.spinbox.value()
        print(value)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()