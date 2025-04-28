import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import AddProduct

import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()

class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI()

        self.show()

    def UI(self):
        pass

    def layout(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame()