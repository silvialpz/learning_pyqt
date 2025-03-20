import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 400, 400)
        self.setWindowTitle("Vertical Box Layout")
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()

        vbox.addStretch()  # Push to the bottom
        btn_1 = QPushButton("Save")
        btn_2 = QPushButton("Exit")
        btn_3 = QPushButton("Hello")
        vbox.addWidget(btn_1)
        vbox.addWidget(btn_2)
        vbox.addWidget((btn_3))
        vbox.addStretch()  # Push back up, to center vertically

        self.setLayout(vbox)

        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()