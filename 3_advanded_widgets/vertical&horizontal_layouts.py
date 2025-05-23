import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 400, 400)
        self.setWindowTitle("Vertical and Horizontal Box Layout")
        self.UI()

    def UI(self):
        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        btn1 = QPushButton()
        btn2 = QPushButton()

        top_layout.setContentsMargins(150, 10, 20, 20)  # (left, top, right, bottom)
        top_layout.addWidget(cbox)
        top_layout.addWidget(rbtn)
        top_layout.addWidget(combo)

        bottom_layout.setContentsMargins(150, 10, 200, 10)
        bottom_layout.addWidget(btn1)
        bottom_layout.addWidget(btn2)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()