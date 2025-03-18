import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350) # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using labels")
        self.UI()

    def UI(self):
        text1 = QLabel("Hello Python", self)
        text2 = QLabel("Hello World", self)
        text1.move(100, 50) # if you don't move the text it will overlap at the origin
        text2.move(200, 50)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()