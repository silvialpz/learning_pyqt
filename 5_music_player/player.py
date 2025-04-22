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
        self.widgets()
        self.layouts()

    def widgets(self):
        self.progress_bar = QProgressBar()


    def layouts(self):
        ########################## Creating Layouts #############################
        self.main_layout = QVBoxLayout()
        self.top_main_layout = QVBoxLayout()
        self.top_group_box = QGroupBox("Music Player", self)  # Group box is a widget, not a layout
        self.top_group_box.setStyleSheet("background-color: orange;")
        self.top_layout = QHBoxLayout()
        self.middle_layout = QHBoxLayout()
        self.bottom_layout = QVBoxLayout()

        ######################### Adding Widgets ############################
        ######################### Top Layout Widgets ############################
        self.top_layout.addWidget(self.progress_bar)
        self.top_main_layout.addLayout(self.top_layout)
        self.top_main_layout.addLayout(self.middle_layout)
        self.top_group_box.setLayout(self.top_main_layout)
        self.main_layout.addWidget(self.top_group_box)
        self.main_layout.addLayout(self.bottom_layout)
        self.setLayout(self.main_layout)


def main():
    App = QApplication(sys.argv)
    window = Player()
    sys.exit(App.exec_())

if __name__ =='__main__':
    main()