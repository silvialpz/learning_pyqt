import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 400, 400)
        self.setWindowTitle("Grid Layout")
        self.UI()

    def UI(self):
        self.grid_layout = QGridLayout()

        # btn1 = QPushButton("Button 1")
        # btn2 = QPushButton("Button 2")
        # btn3 = QPushButton("Button 3")
        # btn4 = QPushButton("Button 4")

        # self.grid_layout.addWidget(btn1, 0, 0)
        # self.grid_layout.addWidget(btn2, 0, 1)
        # self.grid_layout.addWidget(btn3, 1, 0)
        # self.grid_layout.addWidget(btn4, 1, 1)

        for i in range(0, 3):  # rows
            for j in range(0, 3):  # columnns
                btn = QPushButton("Button{}{}".format(i, j))
                self.grid_layout.addWidget(btn, i, j)
                btn.clicked.connect(self.clickMe)

        self.setLayout(self.grid_layout)

        self.show()

    def clickMe(self):
        btn_id = self.sender().text()
        if btn_id == "Button00":
            print("Clicked 0, 0")
        elif btn_id == "Button01":
            print("Clicked 0, 1")
        elif btn_id == "Button02":
            print("Clicked 0, 2")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()