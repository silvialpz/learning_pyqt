import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)  # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using Timer")
        self.UI()

    def UI(self):
        self.color_label = QLabel(self)
        self.color_label.resize(250, 250)
        self.color_label.setStyleSheet("background-color:green")
        self.color_label.move(40, 20)

        ######### Buttons #########
        btn_start = QPushButton("Start", self)
        btn_start.move(80, 300)
        btn_start.clicked.connect(self.start)

        btn_stop = QPushButton("Stop", self)
        btn_stop.move(190, 300)
        btn_stop.clicked.connect(self.stop)

        ######### Timer #########
        self.timer = QTimer()
        self.timer.setInterval(1000)  # milliseconds
        self.timer.timeout.connect(self.change_color)

        self.value = 0

        self.show()

    def change_color(self):
        if self.value == 0:
            self.color_label.setStyleSheet("background-color:yellow")
            self.value = 1
        else:
            self.color_label.setStyleSheet("background-color:red")
            self.value = 0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

def main():
    App = QApplication(sys.argv)
    window = Window()
    # window.start()  # You can also start your timer as soon as you start your application
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()