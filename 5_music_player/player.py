import os, sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, QTimer
from pygame import mixer
from mutagen.mp3 import MP3

mixer.init()

class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(450, 150, 500, 700)
        self.UI()
        self.show()

        self.music_list = []
        self.mute = False
        self.count = 0
        self.song_length = 0

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        self.progress_bar = QProgressBar()

        ########################## Buttons #############################
        self.add_button = QToolButton()
        self.add_button.setIcon(QIcon("icons/add.png"))
        self.add_button.setIconSize(QSize(48, 48))
        self.add_button.setToolTip("Add song")
        self.add_button.clicked.connect(self.addSound)

        self.shuffle_button = QToolButton()
        self.shuffle_button.setIcon(QIcon("icons/shuffle.png"))
        self.shuffle_button.setIconSize(QSize(48, 48))
        self.shuffle_button.setToolTip("Shuffle the list")
        self.shuffle_button.clicked.connect(self.shufflePlaylist)

        self.previous_button = QToolButton()
        self.previous_button.setIcon(QIcon("icons/previous.png"))
        self.previous_button.setIconSize(QSize(48, 48))
        self.previous_button.setToolTip("Play previous")

        self.play_button = QToolButton()
        self.play_button.setIcon(QIcon("icons/play.png"))
        self.play_button.setIconSize(QSize(64, 64))
        self.play_button.setToolTip("Play")
        self.play_button.clicked.connect(self.playSound)

        self.next_button = QToolButton()
        self.next_button.setIcon(QIcon("icons/next.png"))
        self.next_button.setIconSize(QSize(48, 48))
        self.next_button.setToolTip("Play next song")

        self.mute_button = QToolButton()
        self.mute_button.setIcon(QIcon("icons/mute.png"))
        self.mute_button.setIconSize(QSize(24, 24))
        self.mute_button.setToolTip("Mute")
        self.mute_button.clicked.connect(self.muteSound)

        ########################## Volume Slider #############################
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setToolTip("Volume")
        self.volume_slider.setValue(70)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.valueChanged.connect(self.setVolume)

        ########################## Playlist #############################
        self.playlist = QListWidget()
        self.playlist.doubleClicked.connect(self.playSound)

        ########################## Timer #############################
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateProgressBar)

    def layouts(self):
        ########################## Creating Layouts #############################
        self.main_layout = QVBoxLayout()
        self.top_main_layout = QVBoxLayout()
        self.top_group_box = QGroupBox("Music Player")  # Group box is a widget, not a layout
        self.top_group_box.setStyleSheet("background-color: orange;")
        self.top_layout = QHBoxLayout()
        self.middle_layout = QHBoxLayout()
        self.bottom_layout = QVBoxLayout()

        ######################### Adding Widgets ############################
        ######################### Top Layout Widgets ############################
        self.top_layout.addWidget(self.progress_bar)

        ######################### Middle Layout Widgets ############################
        self.middle_layout.addStretch()
        self.middle_layout.addWidget(self.add_button)
        self.middle_layout.addWidget(self.shuffle_button)
        self.middle_layout.addWidget(self.previous_button)
        self.middle_layout.addWidget(self.play_button)
        self.middle_layout.addWidget(self.next_button)
        self.middle_layout.addWidget(self.volume_slider)
        self.middle_layout.addWidget(self.mute_button)
        self.middle_layout.addStretch()

        ######################### Bottom Layout Widgets ############################
        self.bottom_layout.addWidget(self.playlist)


        self.top_main_layout.addLayout(self.top_layout)
        self.top_main_layout.addLayout(self.middle_layout)
        self.top_group_box.setLayout(self.top_main_layout)
        self.main_layout.addWidget(self.top_group_box, 25)
        self.main_layout.addLayout(self.bottom_layout, 75)
        self.setLayout(self.main_layout)

    def addSound(self):
        directory = QFileDialog.getOpenFileName(self, "Add Sound", "", "Sound Files (*.mp3 *.ogg *.wav)")
        filename = os.path.basename(directory[0])
        self.playlist.addItem(filename)
        self.music_list.append(directory[0])

    def shufflePlaylist(self):
        random.shuffle(self.music_list)
        self.playlist.clear()
        for song in self.music_list:
            filename = os.path.basename(song)
            self.playlist.addItem(filename)

    def playSound(self):
        index = self.playlist.currentRow()
        try:
            self.count = 0
            self.progress_bar.setValue(0)
            mixer.music.load(self.music_list[index])
            mixer.music.play()
            self.timer.start()
            sound = MP3(str(self.music_list[index]))
            self.song_length = round(sound.info.length)
            self.progress_bar.setMaximum(self.song_length)
        except:
            pass

    def setVolume(self):
        volume = self.volume_slider.value()
        mixer.music.set_volume(volume/100)

    def muteSound(self):
        if not self.mute:
            self.volume_slider.setValue(0)
            self.mute = True
            self.mute_button.setToolTip("Unmute")
        else:
            self.volume_slider.setValue(70)
            self.mute = False
            self.mute_button.setToolTip("Mute")

    def updateProgressBar(self):
        self.count += 1
        self.progress_bar.setValue(self.count)
        if self.count == self.song_length:
            self.timer.stop()


def main():
    App = QApplication(sys.argv)
    window = Player()
    sys.exit(App.exec_())

if __name__ =='__main__':
    main()