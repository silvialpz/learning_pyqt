import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 400, 400)
        self.setWindowTitle("Horizontal Box Layout")
        self.UI()

    def UI(self):
        hbox = QHBoxLayout()  # No self parameter when you create your horizontal layout

        hbox.addStretch()  # Push to the right
        btn_1 = QPushButton("Button1")
        btn_2 = QPushButton("Button2")
        btn_3 = QPushButton("Button3")
        hbox.addWidget(btn_1)
        hbox.addWidget(btn_2)
        hbox.addWidget(btn_3)
        hbox.addStretch()  # Push to the left, centering the buttons

        self.setLayout(hbox)

        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()