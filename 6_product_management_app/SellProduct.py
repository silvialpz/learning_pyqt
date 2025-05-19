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

        self.UI()

        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

        product_query = "SELECT id, name, quota, price FROM products WHERE availability = 'Available'"
        self.products = cur.execute(product_query).fetchall()

        member_query = "SELECT id, name, surname FROM members"
        self.members = cur.execute(member_query).fetchall()

        for (id, name, quota, price) in self.products:
            self.product_combo_box.addItem(name, id)

        for (id, name, surname) in self.members:
            self.member_combo_box.addItem("{} {}".format(name, surname), id)

        self.set_quantity_combo_box()

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
        self.submit_btn.clicked.connect(self.sell_product)

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

    def sell_product(self):
        sale_data = {
            "product_id": self.product_combo_box.currentData(),
            "product_name": self.product_combo_box.currentText(),
            "member_id": self.member_combo_box.currentData(),
            "member_name": self.member_combo_box.currentText(),
            "quantity": self.quantity_combo_box.currentText(),
            "price": self.products[self.product_combo_box.currentIndex()][3],
            "quota": self.products[self.product_combo_box.currentIndex()][2]
        }

        self.confirm = ConfirmWindow(sale_data)

        self.close()


class ConfirmWindow(QWidget):
    def __init__(self, sale_data):
        super().__init__()
        self.setWindowTitle("Product Sale")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.default_img = 'icons/sell.png'
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())

        self.sale_data = sale_data

        self.UI()

        self.show()

    def UI(self):
        self.widgets()
        self.layouts()


    def widgets(self):
        self.img =  QLabel()
        self.img.setPixmap(QPixmap('icons/sell.png'))
        self.img.setAlignment(Qt.AlignCenter)
        self.title_text = QLabel("Confirm Sale")
        self.title_text.setAlignment(Qt.AlignCenter)

        self.product_text = QLabel(self.sale_data["product_name"])
        self.member_text = QLabel(self.sale_data["member_name"])

        price = int(self.sale_data["price"])
        quantity = int(self.sale_data["quantity"])
        total = quantity * price
        self.sale_data["amount"] = total
        self.quantity_text = QLabel("{}x{} = ${}".format(price, quantity, total))

        self.confirm_btn = QPushButton("Confirm")
        self.confirm_btn.clicked.connect(self.confirm)

    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame()

        self.top_layout.addWidget(self.img)
        self.top_layout.addWidget(self.title_text)
        self.top_frame.setLayout(self.top_layout)

        self.bottom_layout.addRow(QLabel("Product: "), self.product_text)
        self.bottom_layout.addRow(QLabel("Member: "), self.member_text)
        self.bottom_layout.addRow(QLabel("Amount: "), self.quantity_text)
        self.bottom_layout.addRow(QLabel(""), self.confirm_btn)
        self.bottom_frame.setLayout(self.bottom_layout)

        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)

    def confirm(self):
        try:
            sell_query = "INSERT INTO 'sellings' (product_id, member_id, quantity, amount) VALUES (?, ?, ?, ?)"
            cur.execute(sell_query,
                        (
                            self.sale_data["product_id"],
                            self.sale_data["member_id"],
                            self.sale_data["quantity"],
                            self.sale_data["amount"]
                        )
            )
            con.commit()

            if int(self.sale_data["quantity"]) == int(self.sale_data["quota"]):
                sold_out_query = "UPDATE 'products' SET availability='Unavailable' WHERE id=?"
                cur.execute(sold_out_query, (self.sale_data["product_id"], ))
                con.commit()

            update_quota_query = "UPDATE 'products' SET quota=? WHERE id=?"
            cur.execute(update_quota_query, (int(self.sale_data["quota"]) - int(self.sale_data["quantity"]), self.sale_data["product_id"]))
            con.commit()
            QMessageBox.information(self, "Info", "Sale is processed.")
            self.close()
        except:
            QMessageBox.information(self, "Info", "Sale has not been processed.")
