import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image

import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()

class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.default_img = 'icons/sell.png'
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
        self.upload_btn.clicked.connect(self.upload_img)

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.add_product)

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

    def upload_img(self):
        self.default_img = 'icons/sell.png'
        size = (256, 256)
        file_name, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")
        if ok:
            self.default_img = os.path.basename(file_name)
            img = Image.open(file_name)
            img = img.resize(size)
            img.save('img/{0}'.format(self.default_img))
        else:
            self.default_img = "sell.png"

    def add_product(self):
        name = self.name_entry.text()
        manufacturer = self.manufacturer_entry.text()
        price = self.price_entry.text()
        quota = self.quota_entry.text()

        if name and manufacturer and price and quota is not None:
            try:
                query = "INSERT INTO 'products' (name, manufacturer, price, quota, img) VALUES(?, ?, ?, ?, ?)"
                print("hey")
                cur.execute(query, (name, manufacturer, price, quota, self.default_img))
                con.commit()
                QMessageBox.information(self, "Info", "Product has been added")
                con.close()
                self.name_entry.setText("")
                self.manufacturer_entry.setText("")
                self.price_entry.setText("")
                self.quota_entry.setText("")
            except:
                QMessageBox.information(self, "Info", "Product has not been added")
        else:
            QMessageBox.information(self, "Info", "Fields cannot be empty")
