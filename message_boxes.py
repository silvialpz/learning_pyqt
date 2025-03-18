import sysx
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont  # This is how you can use fonts

font = QFont("Times New Roman", 12)  # (font family, font size)
                                     # Check available fonts in Font Book

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)  # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using Message Boxes")
        self.UI()

    def UI(self):
        button = QPushButton("Click me", self)
        button.setFont(font)
        button.move(200, 150)

        button.clicked.connect(self.message_box)

        self.show()

    def message_box(self):
        # mbox = QMessageBox.question(self, "Warning!", "Are you sure to exit?",
        #                            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
        #                            QMessageBox.No) # (parent: self means my window, box title, message, options)

        # if mbox == QMessageBox.Yes:
        #    sys.exit()
        # elif mbox == QMessageBox.No:
        #    print("You clicked No button")

        mbox = QMessageBox.information(self, "Information", "You logged out!")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()