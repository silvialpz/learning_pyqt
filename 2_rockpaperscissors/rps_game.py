import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 500, 500)  # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Rock Paper Scissors Game")
        self.UI()

    def UI(self):

        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    # window.start()  # You can also start your timer as soon as you start your application
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()