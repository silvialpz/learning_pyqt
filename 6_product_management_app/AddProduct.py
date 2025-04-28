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
        self.widgets()
        self.layouts()

    def widgets(self):
        self.img =  QLabel()
        self.img.setPixmap(QPixmap('icons/addproduct.png'))
        self.title_text = QLabel("Add Product")

        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Enter name of product")
        self.manufacturer_entry = QLineEdit()
        self.manufacturer_entry.setPlaceholderText("Enter manufacturer of product")
        self.price_entry = QLineEdit()
        self.price_entry.setPlaceholderText("Enter price of product")
        self.quota_entry = QLineEdit()
        self.quota_entry.setPlaceholderText("Enter quota of product")
        self.upload_btn = QPushButton("Upload")
        self.submit_btn = QPushButton("Submit")

    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame()

        self.top_layout.addWidget(self.img)
        self.top_layout.addWidget(self.title_text)
        self.top_frame.setLayout(self.top_layout)

        self.bottom_layout.addRow(QLabel("Name: "), self.name_entry)
        self.bottom_layout.addRow(QLabel("Manufacturer: "), self.manufacturer_entry)
        self.bottom_layout.addRow(QLabel("Price: "), self.price_entry)
        self.bottom_layout.addRow(QLabel("Quota: "), self.quota_entry)
        self.bottom_layout.addRow(QLabel("Upload: "), self.upload_btn)
        self.bottom_layout.addRow(QLabel(""), self.submit_btn)
        self.bottom_frame.setLayout(self.bottom_layout)

        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)



