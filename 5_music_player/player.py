import sys
from PyQt5.QtWidgets import *

class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(450, 150, 400, 700)
        self.UI()
        self.show()

    def UI(self):
        pass

    def layout(self):
        self.main_layout = QVBoxLayout()
        self.top_main_layout = QVBoxLayout()
        self.top_group_box = QGroupBox("Music Player", self)
        self.top_layout = QHBoxLayout()
        self.middle_layout = QHBoxLayout()
        self.bottom_layout = QVBoxLayout()


def main():
    App = QApplication(sys.argv)
    window = Player()
    sys.exit(App.exec_())

if __name__ =='__main__':
    main()