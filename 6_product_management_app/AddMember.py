import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image

import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()

class AddMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Member")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI()

        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        self.add_member_img = QLabel()
        img = QPixmap('icons/addmember.png')
        self.add_member_img.setPixmap(img)
        self.add_member_img.setAlignment(Qt.AlignCenter)
        self.title_text = QLabel("Add Member")
        self.title_text.setAlignment(Qt.AlignCenter)

        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Name of Member")
        self.surname_entry = QLineEdit()
        self.surname_entry.setPlaceholderText("Surname of Member")
        self.phone_entry = QLineEdit()
        self.phone_entry.setPlaceholderText("Enter Member Phone")
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.add_member)

    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame()

        self.top_layout.addWidget(self.add_member_img)
        self.top_layout.addWidget(self.title_text)
        self.top_frame.setLayout(self.top_layout)

        self.bottom_layout.addRow("Name: ", self.name_entry)
        self.bottom_layout.addRow("Surname: ", self.surname_entry)
        self.bottom_layout.addRow("Phone: ", self.phone_entry)
        self.bottom_layout.addRow("", self.submit_btn)
        self.bottom_frame.setLayout(self.bottom_layout)

        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)

        self.setLayout(self.main_layout)

    def add_member(self):
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = self.phone_entry.text()

        if name and surname and phone is not None:
            try:
                query = "INSERT INTO 'members' (name, surname, phone) VALUES(?, ?, ?)"
                con.execute(query, (name, surname, phone))
                con.commit()
                QMessageBox.information(self, "Info", "Member has been added")
                self.name_entry.setText("")
                self.surname_entry.setText("")
                self.phone_entry.setText("")
            except:
                QMessageBox.information(self, "Info", "Member has not been added")
        else:
            QMessageBox.information(self, "Info", "Fields cannot be empty")
