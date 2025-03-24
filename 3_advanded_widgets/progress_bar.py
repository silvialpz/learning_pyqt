import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *

count = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 400, 400)
        self.setWindowTitle("Progress Bar Widget")
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.progressbar = QProgressBar()
        btn_start = QPushButton("Start")
        btn_start.clicked.connect(self.timerStart)
        btn_stop = QPushButton("Stop")
        btn_stop.clicked.connect(self.timerStop)
        self.timer = QTimer()
        self.timer.setInterval(1000)  # milliseconds
        self.timer.timeout.connect(self.runProgressbar)

        vbox.addWidget(self.progressbar)
        vbox.addLayout(hbox)
        hbox.addWidget(btn_start)
        hbox.addWidget(btn_stop)

        self.setLayout(vbox)


        self.show()

    def timerStart(self):
        self.timer.start()

    def timerStop(self):
        self.timer.stop()

    def runProgressbar(self):
        global count
        count += 1
        print(count)
        self.progressbar.setValue(count)  # percentages

        if count == 100:
            self. timer.stop()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()