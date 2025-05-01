import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

import AddProduct
import AddMember

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
        self.tabWidgets()
        self.widgets()
        self.layouts()
        self.display_products()
        self.display_members()

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

    def tabWidgets(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Statistics")

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

        self.all_products = QRadioButton("All")
        self.available_products = QRadioButton("Available")
        self.not_available_products = QRadioButton("Not Available")
        self.list_button = QPushButton("List")

        ######################## TAB 2 ########################
        self.members_table = QTableWidget()
        self.members_table.setColumnCount(4)
        self.members_table.setHorizontalHeaderItem(0, QTableWidgetItem("Member ID"))
        self.members_table.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.members_table.setHorizontalHeaderItem(2, QTableWidgetItem("Surname"))
        self.members_table.setHorizontalHeaderItem(3, QTableWidgetItem("Phone Number"))

        self.member_search_text = QLabel("Search Member:")
        self.member_search_entry = QLineEdit()
        self.member_search_button = QPushButton("Search")


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
        self.member_main_layout =  QHBoxLayout()
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

    def func_add_product(self):
        self.new_product = AddProduct.AddProduct()

    def func_add_member(self):
        self.new_member = AddMember.AddMember()

    def display_products(self):
        self.products_table.setFont(QFont("Tahoma", 16))
        for i in reversed(range(self.products_table.rowCount())):
            self.products_table.removeRow(i)

        query = cur.execute("SELECT id, name, manufacturer, price, quota, availability FROM products")
        for row_data in query:
            row_number = self.products_table.rowCount()
            self.products_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.products_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.products_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def display_members(self):
        self.members_table.setFont(QFont("Tahoma", 16))

        for i in reversed(range(self.members_table.rowCount())):
            self.members_table.removeRow(i)

        query = cur.execute("SELECT * FROM members")
        for row_data in query:
            row_number = self.members_table.rowCount()
            self.members_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.members_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.members_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def selected_product(self):
        list_product = []
        for i in range(0, 6):
            list_product.append(self.products_table.item(self.products_table.currentRow(), i).text())

        self.display = DisplayProduct()

class DisplayProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450, 150, 350, 600)
        self.setFixedSize(self.size())

        self.UI()
        self.show()

    def UI(self):
        pass


def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
