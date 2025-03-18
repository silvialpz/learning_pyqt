import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont  # This is how you can use fonts

font = QFont("Times New Roman", 14)  # (font family, font size)
                                     # Check available fonts in Font Book

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)  # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using Text Editor")
        self.UI()

    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(150, 80)
        self.editor.setAcceptRichText(False)  # This Text Editor also accepts Rich Text (With formatting and stuff)

        button = QPushButton("Send", self)
        button.move(330, 280)
        button.clicked.connect(self.get_value)

        self.show()

    def get_value(self):
        text = self.editor.toPlainText()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()