import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

txt_font = QFont("Times New Roman", 25)
btn_font = QFont("Arial", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 500, 500)  # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Rock Paper Scissors Game")
        self.UI()

    def UI(self):
        ####################### Scores #######################
        self.score_computer_txt = QLabel("Computer Score:", self)
        self.score_computer_txt.move(30, 20)
        self.score_computer_txt.setFont(txt_font)

        self.score_player_txt = QLabel("Your Score:", self)
        self.score_player_txt.move(330, 20)
        self.score_player_txt.setFont(txt_font)

        ####################### Images #######################
        self.image_computer = QLabel(self)
        self.image_computer.setPixmap(QPixmap("images/rock.png"))
        self.image_computer.move(50, 100)

        self.image_player = QLabel(self)
        self.image_player.setPixmap(QPixmap("images/rock.png"))
        self.image_player.move(330, 100)

        self.image_game = QLabel(self)
        self.image_game.setPixmap(QPixmap("images/game.png"))
        self.image_game.move(230, 100)

        ####################### Buttons #######################
        btn_start = QPushButton("Start", self)
        btn_start.setFont(btn_font)
        btn_start.move(180, 250)
        btn_start.clicked.connect(self.start)

        btn_stop = QPushButton("Stop", self)
        btn_stop.setFont(btn_font)
        btn_stop.move(270, 250)
        btn_stop.clicked.connect(self.stop)

        ####################### Timer #######################
        self.timer = QTimer(self)
        self.timer.setInterval(100)  # milliseconds
        self.timer.timeout.connect(self.playGame)

        self.show()

    def playGame(self):
        self.rnd_computer = randint(1, 3)
        if self.rnd_computer == 1:
            self.image_computer.setPixmap(QPixmap("images/rock.png"))
        elif self.rnd_computer == 2:
            self.image_computer.setPixmap(QPixmap("images/paper.png"))
        else:
            self.image_computer.setPixmap(QPixmap("images/scissors.png"))

        self.rnd_player = randint(1, 3)
        if self.rnd_player == 1:
            self.image_player.setPixmap(QPixmap("images/rock.png"))
        elif self.rnd_player == 2:
            self.image_player.setPixmap(QPixmap("images/paper.png"))
        else:
            self.image_player.setPixmap(QPixmap("images/scissors.png"))

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