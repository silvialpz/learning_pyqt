import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
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

        product_query = "SELECT id, name, quota FROM products WHERE availability = 'Available'"
        self.products = cur.execute(product_query).fetchall()

        member_query = "SELECT id, name, surname FROM members"
        self.members = cur.execute(member_query).fetchall()

        self.UI()

        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        self.img =  QLabel()
        self.img.setPixmap(QPixmap('icons/sell.png'))
        self.img.setAlignment(Qt.AlignCenter)
        self.title_text = QLabel("Sell Product")
        self.title_text.setAlignment(Qt.AlignCenter)

        self.product_combo_box = QComboBox()
        self.product_combo_box.currentIndexChanged.connect(self.set_quantity_combo_box)
        self.member_combo_box = QComboBox()
        self.quantity_combo_box = QComboBox()

        self.submit_btn = QPushButton("Submit")

        for (id, name, quota) in self.products:
            self.product_combo_box.addItem(name, id)

        for (id, name, surname) in self.members:
            self.member_combo_box.addItem("{} {}".format(name, surname), id)

        self.set_quantity_combo_box()

    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame()

        self.top_layout.addWidget(self.img)
        self.top_layout.addWidget(self.title_text)
        self.top_frame.setLayout(self.top_layout)

        self.bottom_layout.addRow(QLabel("Product: "), self.product_combo_box)
        self.bottom_layout.addRow(QLabel("Member: "), self.member_combo_box)
        self.bottom_layout.addRow(QLabel("Quantity: "), self.quantity_combo_box)
        self.bottom_layout.addRow(QLabel(""), self.submit_btn)
        self.bottom_frame.setLayout(self.bottom_layout)

        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)

    def set_quantity_combo_box(self):
        self.quantity_combo_box.clear()
        product_quantity = self.products[self.product_combo_box.currentIndex()][2]
        for i in range(1, product_quantity+1):
            self.quantity_combo_box.addItem(str(i))