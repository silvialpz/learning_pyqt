from PyQt5.QtWidgets import *
import sys

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees")
        self.setGeometry(450, 150, 750, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):
        pass

    def layouts(self):
        self.main_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()

        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)

        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_main_layout)

        self.setLayout(self.main_layout)


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
