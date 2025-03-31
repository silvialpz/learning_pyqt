from PyQt5.QtWidgets import *
import sqlite3
import sys

connection = sqlite3.connect('employees.db')
cursor = connection.cursor()

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees")
        self.setGeometry(450, 150, 750, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):
        self.employee_list = QListWidget()
        self.btn_new = QPushButton("New")
        self.btn_new.clicked.connect(self.addEmployee)
        self.btn_edit = QPushButton("Edit")
        self.btn_del = QPushButton("Delete")

    def layouts(self):
        ####################### Layouts #######################
        self.main_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()
        ####################### Adding Layouts #######################
        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)

        self.main_layout.addLayout(self.left_layout, 40)  # using aspect ratio for layout
        self.main_layout.addLayout(self.right_main_layout, 60)
        ####################### Adding Widgets #######################
        self.right_top_layout.addWidget(self.employee_list)
        self.right_bottom_layout.addWidget(self.btn_new)
        self.right_bottom_layout.addWidget(self.btn_edit)
        self.right_bottom_layout.addWidget(self.btn_del)
        ####################### Main Window Layout #######################
        self.setLayout(self.main_layout)

    def addEmployee(self):
        self.newEmployee = AddEmployee()
        self.close()

# make a class for each window
class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employees")
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):
        pass

    def layouts(self):
        ####################### Main Layouts #######################
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        ####################### Adding Layouts #######################
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)

        self.setLayout(self.main_layout)

def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
