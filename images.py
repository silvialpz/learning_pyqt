import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap # needed to display images

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500) # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using images")
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('images/moana.jpg'))
        self.image.move(150, 50)

        remove_button = QPushButton("remove", self)
        remove_button.move(150, 220)
        remove_button.clicked.connect(self.remove_image)

        show_button = QPushButton("show", self)
        show_button.move(260, 220)
        show_button.clicked.connect(self.show_image)

        self.show()

    def remove_image(self):
        self.image.close()

    def show_image(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()