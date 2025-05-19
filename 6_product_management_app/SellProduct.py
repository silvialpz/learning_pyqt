import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image

import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()

class SellProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sell Product")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.default_img = 'icons/sell.png'
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI()

        self.show()

    def UI(self):
        pass