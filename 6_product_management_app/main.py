import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image

import AddProduct
import AddMember
import SellProduct

import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Management")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(100, 50, 1350, 750)

        self.UI()
        self.show()

    def UI(self):
        self.toolbar()
        self.widgets()
        self.tabWidgets()
        self.layouts()
        self.display_products()
        self.display_members()
        self.display_statistics()

    def toolbar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.add_product = QAction(QIcon('icons/add.png'), "Add Product", self)
        self.tb.addAction(self.add_product)
        self.tb.addSeparator()
        self.add_product.triggered.connect(self.func_add_product)

        self.add_member = QAction(QIcon('icons/user.png'), "Add Member", self)
        self.tb.addAction(self.add_member)
        self.tb.addSeparator()
        self.add_member.triggered.connect(self.func_add_member)

        self.sell_product = QAction(QIcon('icons/sell.png'), "Sell Product", self)
        self.tb.addAction(self.sell_product)
        self.tb.addSeparator()
        self.sell_product.triggered.connect(self.func_sell_product)

    def tabWidgets(self):
        self.tabs = QTabWidget()
        self.tabs.currentChanged.connect(self.update_tabs)
        self.setCentralWidget(self.tabs)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Statistics")

    def update_tabs(self):
        self.display_members()
        self.display_products()
        self.display_statistics()

    def widgets(self):
        ######################## TAB 1 ########################
        self.products_table = QTableWidget()
        self.products_table.setColumnCount(6)
        self.products_table.setColumnHidden(0, True)
        self.products_table.setHorizontalHeaderItem(0, QTableWidgetItem("Product Id"))
        self.products_table.setHorizontalHeaderItem(1, QTableWidgetItem("Product Name"))
        self.products_table.setHorizontalHeaderItem(2, QTableWidgetItem("Manufacturer"))
        self.products_table.setHorizontalHeaderItem(3, QTableWidgetItem("Price"))
        self.products_table.setHorizontalHeaderItem(4, QTableWidgetItem("Quota"))
        self.products_table.setHorizontalHeaderItem(5, QTableWidgetItem("Availability"))
        self.products_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.products_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.products_table.doubleClicked.connect(self.selected_product)

        self.search_text = QLabel("Search")
        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("Search for Products")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_products)

        self.all_products = QRadioButton("All")
        self.available_products = QRadioButton("Available")
        self.not_available_products = QRadioButton("Not Available")
        self.list_button = QPushButton("List")
        self.list_button.clicked.connect(self.list_products)

        ######################## TAB 2 ########################
        self.members_table = QTableWidget()
        self.members_table.setColumnCount(4)
        self.members_table.setHorizontalHeaderItem(0, QTableWidgetItem("Member ID"))
        self.members_table.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.members_table.setHorizontalHeaderItem(2, QTableWidgetItem("Surname"))
        self.members_table.setHorizontalHeaderItem(3, QTableWidgetItem("Phone Number"))
        self.members_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.members_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.members_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.members_table.doubleClicked.connect(self.selected_member)

        self.member_search_text = QLabel("Search Member:")
        self.member_search_entry = QLineEdit()
        self.member_search_button = QPushButton("Search")
        self.member_search_button.clicked.connect(self.search_members)

        ######################## TAB 3 ########################
        self.statistics_title = QLabel("Statistics")

        self.total_products_text = QLabel("")
        self.total_members_text = QLabel("")
        self.sold_products = QLabel("")
        self.total_amount = QLabel("")

    def layouts(self):
        ######################## TAB 1 ########################
        self.main_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_middle_layout = QHBoxLayout()
        self.top_group_box = QGroupBox("Search Box")
        self.middle_group_box = QGroupBox("List Box")

        self.left_layout.addWidget(self.products_table)

        self.right_top_layout.addWidget(self.search_text)
        self.right_top_layout.addWidget(self.search_entry)
        self.right_top_layout.addWidget(self.search_button)
        self.top_group_box.setLayout(self.right_top_layout)
        self.right_layout.addWidget(self.top_group_box)

        self.right_middle_layout.addWidget(self.all_products)
        self.right_middle_layout.addWidget(self.available_products)
        self.right_middle_layout.addWidget(self.not_available_products)
        self.right_middle_layout.addWidget(self.list_button)
        self.middle_group_box.setLayout(self.right_middle_layout)
        self.right_layout.addWidget(self.middle_group_box)

        self.main_layout.addLayout(self.left_layout, 70)
        self.main_layout.addLayout(self.right_layout, 30)
        self.tab1.setLayout(self.main_layout)

        ######################## TAB 2 ########################
        self.member_main_layout = QHBoxLayout()
        self.member_left_layout = QHBoxLayout()
        self.member_right_layout = QHBoxLayout()
        self.member_right_groupbox = QGroupBox("Search for Members")
        self.member_right_groupbox.setContentsMargins(10, 10, 10, 600)

        self.member_left_layout.addWidget(self.members_table)
        self.member_right_layout.addWidget(self.member_search_text)
        self.member_right_layout.addWidget(self.member_search_entry)
        self.member_right_layout.addWidget(self.member_search_button)

        self.member_right_groupbox.setLayout(self.member_right_layout)

        self.member_main_layout.addLayout(self.member_left_layout, 70)
        self.member_main_layout.addWidget(self.member_right_groupbox, 30)
        self.tab2.setLayout(self.member_main_layout)

        ######################## TAB 3 ########################
        self.statistics_form = QFormLayout()
        self.tab3.setLayout(self.statistics_form)

        self.statistics_form.addRow(self.statistics_title, QLabel(""))
        self.statistics_form.addRow(QLabel("Total Products: "), self.total_products_text)
        self.statistics_form.addRow(QLabel("Total Members: "), self.total_members_text)
        self.statistics_form.addRow(QLabel("Sold Products: "), self.sold_products)
        self.statistics_form.addRow(QLabel("Total Amount: "), self.total_amount)

    def func_add_product(self):
        self.new_product = AddProduct.AddProduct()

    def func_add_member(self):
        self.new_member = AddMember.AddMember()

    def func_sell_product(self):
        self.sell = SellProduct.SellProduct()

    def display_products(self, query=None):
        if query is None:
            query = "SELECT id, name, manufacturer, price, quota, availability FROM products"

        self.products_table.setFont(QFont("Tahoma", 16))
        for i in reversed(range(self.products_table.rowCount())):
            self.products_table.removeRow(i)

        query = cur.execute(query)
        for row_data in query:
            row_number = self.products_table.rowCount()
            self.products_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.products_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.products_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def display_members(self, query=None):
        if query is None:
            query = "SELECT * FROM members"
        self.members_table.setFont(QFont("Tahoma", 16))

        for i in reversed(range(self.members_table.rowCount())):
            self.members_table.removeRow(i)

        query = cur.execute(query)
        for row_data in query:
            row_number = self.members_table.rowCount()
            self.members_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.members_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.members_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def display_statistics(self):
        self.total_products_text.setText(str(self.products_table.rowCount()))
        self.total_members_text.setText(str(self.members_table.rowCount()))

        sales_query = "SELECT quantity, amount FROM 'sellings'"
        sale_data = cur.execute(sales_query).fetchall()

        total_sold_products = 0
        total_amount = 0
        for quantity, amount in sale_data:
            total_sold_products += quantity
            total_amount += amount

        self.sold_products.setText(str(total_sold_products))
        self.total_amount.setText("$ {}".format(total_amount))

    def selected_product(self):
        product_id = self.products_table.item(self.products_table.currentRow(), 0).text()
        self.display = DisplayProduct(product_id)

    def selected_member(self):
        member_id = self.members_table.item(self.members_table.currentRow(), 0).text()
        self.display = DisplayMember(member_id)

    def search_products(self):
        value = self.search_entry.text()

        if value == "":
            QMessageBox.information(self, "Warning", "Search entry cannot be empty")
        else:
            self.search_entry.setText("")
            query = "SELECT id, name, manufacturer, price, quota, availability FROM products WHERE name LIKE '{}' or manufacturer LIKE '{}'".format('%'+value + '%', '%'+value + '%')
            self.display_products(query)

    def search_members(self):
        value = self.member_search_entry.text()

        if value == "":
            QMessageBox.information(self, "Warning", "Search entry cannot be empty")
        else:
            self.search_entry.setText("")
            query = "SELECT id, name, surname, phone FROM members WHERE name LIKE '{}' or surname LIKE '{}'".format('%'+value + '%', '%'+value + '%')
            self.display_members(query)

    def list_products(self):
        if self.all_products.isChecked():
            self.display_products("SELECT id, name, manufacturer, price, quota, availability FROM products")
        elif self.available_products.isChecked():
            self.display_products("SELECT id, name, manufacturer, price, quota, availability FROM products WHERE availability='Available'")
        elif self.not_available_products.isChecked():
            self.display_products("SELECT id, name, manufacturer, price, quota, availability FROM products WHERE availability='Unavailable'")

class DisplayMember(QWidget):
    def __init__(self, member_id):
        super().__init__()
        self.setWindowTitle("Member Details")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450, 150, 350, 600)
        self.setFixedSize(self.size())
        self.member_id = member_id

        self.UI()
        self.show()

    def UI(self):
        self.member_details()
        self.widgets()
        self.layouts()

    def member_details(self):
        query = ("SELECT * FROM members WHERE id=?")
        member = cur.execute(query, (self.member_id,)).fetchone()

        self.name = member[1]
        self.surname = member[2]
        self.phone = member[3]

    def widgets(self):
        self.img = QLabel()
        self.img.setPixmap(QPixmap("icons/user.png"))
        self.img.setAlignment(Qt.AlignCenter)
        self.title_text = QLabel("Update Member")
        self.title_text.setAlignment(Qt.AlignCenter)

        self.name_entry = QLineEdit()
        self.name_entry.setText(self.name)
        self.surname_entry = QLineEdit()
        self.surname_entry.setText(self.surname)
        self.phone_entry = QLineEdit()
        self.phone_entry.setText(self.phone)

        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.delete_member)
        self.update_btn = QPushButton("Update")
        self.update_btn.clicked.connect(self.update_member)

    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame()

        self.top_layout.addWidget(self.title_text)
        self.top_layout.addWidget(self.img)
        self.top_frame.setLayout(self.top_layout)

        self.bottom_layout.addRow(QLabel("Name: "), self.name_entry)
        self.bottom_layout.addRow(QLabel("Surname: "), self.surname_entry)
        self.bottom_layout.addRow(QLabel("Phone: "), self.phone_entry)
        self.bottom_layout.addRow(QLabel(""), self.delete_btn)
        self.bottom_layout.addRow(QLabel(""), self.update_btn)
        self.bottom_frame.setLayout(self.bottom_layout)

        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)

        self.setLayout(self.main_layout)

    def delete_member(self):
        mbox = QMessageBox.warning(self, "Warning", "Are you sure you want to delete this member?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if mbox == QMessageBox.Yes:
            try:
                cur.execute("DELETE FROM members WHERE id=?", (self.member_id,))
                con.commit()
                QMessageBox.information(self, "Info", "Member has been deleted")
                self.close()
            except:
                QMessageBox.information(self, "Info", "Member has not been deleted")

    def update_member(self):
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = int(self.phone_entry.text())

        if name and surname and phone is not None:
            try:
                query = "UPDATE members SET name=?, surname=?, phone=? WHERE id=?"
                cur.execute(query, (name, surname, phone, self.member_id))
                con.commit()
                QMessageBox.information(self, "Info", "Member has been updated")
            except:
                QMessageBox.information(self, "Info", "Member has not been updated")
        else:
            QMessageBox.information(self, "Info", "Fields cannot be empty")


class DisplayProduct(QWidget):
    def __init__(self, product_id):
        super().__init__()
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450, 150, 350, 600)
        self.setFixedSize(self.size())
        self.product_id = product_id

        self.UI()
        self.show()

    def UI(self):
        self.product_details()
        self.widgets()
        self.layouts()

    def product_details(self):
        query = ("SELECT * FROM products WHERE id=?")
        product = cur.execute(query, (self.product_id,)).fetchone()

        self.name = product[1]
        self.manufacturer = product[2]
        self.price = product[3]
        self.quota = product[4]
        self.product_img = "img/{}".format(product[5])
        self.status = product[6]

    def widgets(self):
        self.img = QLabel()
        self.img.setPixmap(QPixmap(self.product_img))
        self.img.setAlignment(Qt.AlignCenter)
        self.title_text = QLabel("Update Product")
        self.title_text.setAlignment(Qt.AlignCenter)

        self.name_entry = QLineEdit()
        self.name_entry.setText(self.name)
        self.manufacturer_entry = QLineEdit()
        self.manufacturer_entry.setText(self.manufacturer)
        self.price_entry = QLineEdit()
        self.price_entry.setText(str(self.price))
        self.quota_entry = QLineEdit()
        self.quota_entry.setText(str(self.quota))
        self.availability_combo = QComboBox()
        self.availability_combo.addItems(["Available", "Unavailable"])
        self.upload_btn = QPushButton("Upload")
        self.upload_btn.clicked.connect(self.upload_img)
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.delete_product)
        self.update_btn = QPushButton("Update")
        self.update_btn.clicked.connect(self.update_product)

    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame()

        self.top_layout.addWidget(self.title_text)
        self.top_layout.addWidget(self.img)
        self.top_frame.setLayout(self.top_layout)

        self.bottom_layout.addRow(QLabel("Name: "), self.name_entry)
        self.bottom_layout.addRow(QLabel("Manufacturer: "), self.manufacturer_entry)
        self.bottom_layout.addRow(QLabel("Price: "), self.price_entry)
        self.bottom_layout.addRow(QLabel("Quota: "), self.quota_entry)
        self.bottom_layout.addRow(QLabel("Status: "), self.availability_combo)
        self.bottom_layout.addRow(QLabel("Image: "), self.upload_btn)
        self.bottom_layout.addRow(QLabel(""), self.delete_btn)
        self.bottom_layout.addRow(QLabel(""), self.update_btn)
        self.bottom_frame.setLayout(self.bottom_layout)

        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)

        self.setLayout(self.main_layout)

    def upload_img(self):
        size = (256, 256)
        file_name, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")
        if ok:
            self.product_img = os.path.basename(file_name)
            img = Image.open(file_name)
            img = img.resize(size)
            img.save('img/{0}'.format(self.product_img))

    def update_product(self):
        name = self.name_entry.text()
        manufacturer = self.manufacturer_entry.text()
        price = int(self.price_entry.text())
        quota = int(self.quota_entry.text())
        status = self.availability_combo.currentText()
        default_img = self.product_img

        if name and manufacturer and price and quota is not None:
            try:
                query = "UPDATE products SET name=?, manufacturer=?, price=?, quota=?, img=?, availability=? WHERE id=?"
                cur.execute(query, (name, manufacturer, price, quota, default_img, status, self.product_id))
                con.commit()
                QMessageBox.information(self, "Info", "Product has been updated")
            except:
                QMessageBox.information(self, "Info", "Product has not been updated")
        else:
            QMessageBox.information(self, "Info", "Fields cannot be empty")

    def delete_product(self):
        mbox = QMessageBox.warning(self, "Warning", "Are you sure you want to delete this product?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if mbox == QMessageBox.Yes:
            try:
                cur.execute("DELETE FROM products WHERE id=?", (self.product_id,))
                con.commit()
                QMessageBox.information(self, "Info", "Product has been deleted")
                self.close()
            except:
                QMessageBox.information(self, "Info", "Product has not been deleted")


def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
