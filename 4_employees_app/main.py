from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
import sqlite3
import sys, os
from PIL import Image

connection = sqlite3.connect('employees.db')
cursor = connection.cursor()
default_img = 'person.png'


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
        self.getEmployees()
        self.displayFirstRecord()

    def mainDesign(self):
        self.setStyleSheet("font-size: 14pt; font-family: Arial; font-weight: bold;")
        self.employee_list = QListWidget()
        self.employee_list.itemClicked.connect(self.singleClick)
        self.btn_new = QPushButton("New")
        self.btn_new.clicked.connect(self.addEmployee)
        self.btn_edit = QPushButton("Edit")
        self.btn_edit.clicked.connect(self.editEmployee)
        self.btn_del = QPushButton("Delete")
        self.btn_del.clicked.connect(self.deleteEmployee)

    def layouts(self):
        ####################### Layouts #######################
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
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

    def getEmployees(self):
        query = "SELECT id, name, surname FROM employees"
        employees = cursor.execute(query).fetchall()

        for (number, name, surname) in employees:
            # Use employee number in order to be able to update records with ID
            self.employee_list.addItem("{} -  {} {}".format(number, name, surname))

    def displayFirstRecord(self):
        # Check table is not empty
        query = "SELECT COUNT(*) FROM employees"
        count = cursor.execute(query).fetchone()
        if count == (0, ):
            return

        query = "SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee = cursor.execute(query).fetchone()
        number, name_text, surname_text, phone_text, email_text, img_addr, address_text = employee

        img = QLabel()
        img.setPixmap(QPixmap("images/{}".format(img_addr)))
        name = QLabel(name_text)
        surname = QLabel(surname_text)
        phone = QLabel(phone_text)
        email = QLabel(email_text)
        address = QLabel(address_text)

        self.left_layout.setVerticalSpacing(20)
        self.left_layout.addRow("", img)
        self.left_layout.addRow("Name: ", name)
        self.left_layout.addRow("Surname: ", surname)
        self.left_layout.addRow("Phone: ", phone)
        self.left_layout.addRow("Email: ", email)
        self.left_layout.addRow("Address: ", address)

    def singleClick(self):
        # remove existing widgets in left panel
        for i in reversed(range(self.left_layout.count())):
            widget = self.left_layout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        person = self.employee_list.currentItem().text()
        id_number, name = person.split(" - ")
        query = "SELECT * FROM employees WHERE id=?"
        employee = cursor.execute(query, (id_number, )).fetchone()  # single item tuple

        number, name_text, surname_text, phone_text, email_text, img_addr, address_text = employee

        img = QLabel()
        img.setPixmap(QPixmap("images/{}".format(img_addr)))
        name = QLabel(name_text)
        surname = QLabel(surname_text)
        phone = QLabel(phone_text)
        email = QLabel(email_text)
        address = QLabel(address_text)

        self.left_layout.setVerticalSpacing(20)
        self.left_layout.addRow("", img)
        self.left_layout.addRow("Name: ", name)
        self.left_layout.addRow("Surname: ", surname)
        self.left_layout.addRow("Phone: ", phone)
        self.left_layout.addRow("Email: ", email)
        self.left_layout.addRow("Address: ", address)

    def deleteEmployee(self):
        if self.employee_list.selectedItems():  # Check employee is selected
            person = self.employee_list.currentItem().text()
            id_number, name = person.split(" - ")

            mbox = QMessageBox.question(self, "Warning", "Do you want to delete this person?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM employees WHERE id=?"
                    cursor.execute(query, (id_number, ))
                    connection.commit()
                    QMessageBox.information(self, "Info", "Employee has been deleted")
                    self.close()
                    self.main = Main()
                except:
                    QMessageBox.information(self, "Warning!", "Employee has not been deleted")
        else:
            QMessageBox.information(self, "Info", "Please select a person to delete")

    def editEmployee(self):
        if self.employee_list.selectedItems():
            person = self.employee_list.currentItem().text()
            id_number, name = person.split(" - ")
            self.updateWindow = EditEmployee(id_number)
            self.close()
        else:
            QMessageBox.information(self, "Info", "Please select a person to update")


# make a class for each window
class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employee")
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.setFocus()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def closeEvent(self, event):
        self.main = Main()  # you create another instance of the Main window to go back to

    def mainDesign(self):
        self.setStyleSheet("background-color: white; font-size: 14pt; font-family: Times New Roman; color: black;")
        ##################### Top Layout Widgets ######################
        self.title = QLabel("Add Person")
        self.title.setStyleSheet("font-size: 24pt; font-family: Arial; font-weight: bold;")  # The style sheet set for the title has preference over the ones set for the window
        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap('icons/person.png'))
        ##################### Bottom Layout Widgets ######################
        self.name_lbl = QLabel("Name: ")
        self.name_entry = QLineEdit()
        self.name_entry.setMinimumWidth(210)
        self.name_entry.setPlaceholderText("Enter Employee Name")
        self.surname_lbl = QLabel("Surname: ")
        self.surname_entry = QLineEdit()
        self.surname_entry.setMinimumWidth(210)
        self.surname_entry.setPlaceholderText("Enter Employee Surname")
        self.phone_lbl = QLabel("Phone: ")
        self.phone_entry = QLineEdit()
        self.phone_entry.setMinimumWidth(210)
        self.phone_entry.setPlaceholderText("Enter Employee Phone Number")
        self.email_lbl = QLabel("Email: ")
        self.email_entry = QLineEdit()
        self.email_entry.setMinimumWidth(210)
        self.email_entry.setPlaceholderText("Enter Employee Email")
        self.img_lbl = QLabel("Picture: ")
        self.img_btn = QPushButton("Browse")
        self.img_btn.setStyleSheet("background-color: orange;")
        self.img_btn.clicked.connect(self.uploadImage)
        self.addr_lbl = QLabel("Address: ")
        self.addr_editor = QTextEdit()
        self.add_btn = QPushButton("Add")
        self.add_btn.setStyleSheet("background-color: orange;")
        self.add_btn.clicked.connect(self.addEmployee)

    def layouts(self):
        ####################### Main Layouts #######################
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        ####################### Adding Layouts #######################
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)
        ####################### Adding Widgets to Top Layout #######################
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget(self.img_add)
        self.top_layout.addStretch()
        self.top_layout.setContentsMargins(110, 20, 10, 30)  # left, top, right, bottom
        ####################### Adding Widgets to Bottom Layout #######################
        self.bottom_layout.addRow(self.name_lbl, self.name_entry)
        self.bottom_layout.addRow(self.surname_lbl, self.surname_entry)
        self.bottom_layout.addRow(self.phone_lbl, self.phone_entry)
        self.bottom_layout.addRow(self.email_lbl, self.email_entry)
        self.bottom_layout.addRow(self.img_lbl, self.img_btn)
        self.bottom_layout.addRow(self.addr_lbl, self.addr_editor)
        self.bottom_layout.addRow("", self.add_btn)
        ####################### Main Window Layout #######################
        self.setLayout(self.main_layout)

    def uploadImage(self):
        global default_img
        size = (128, 128)
        self.file_name, ok = QFileDialog.getOpenFileName(self, "Upload image", '', 'Image Files (*.jpg *.png)')

        if ok:
            default_img = os.path.basename(self.file_name)
            img = Image.open(self.file_name)
            img = img.resize(size)
            img.save("images/{}".format(default_img))

    def addEmployee(self):
        global default_img
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = self.phone_entry.text()
        email = self.email_entry.text()
        img = default_img
        address = self.addr_editor.toPlainText()

        if (name and surname and phone and email != ""):
            # to add record to database, use try-except blocks
            try:
                query = "INSERT INTO employees (name, surname, phone, email, img, address) VALUES(?, ?, ?, ?, ?, ?)"
                cursor.execute(query, (name, surname, phone, email, img, address))
                connection.commit()  # Use commit each time you update database
                QMessageBox.information(self, "Success", "Employee has been added to database")
                self.close()
                self.main = Main()
            except:
                QMessageBox.information(self, "Warning", "Employee has NOT been added to database")
        else:
            QMessageBox.information(self, "Warning", "Fields cannot be empty")

class EditEmployee(QWidget):
    def __init__(self, person_id):
        super().__init__()
        self.person_id = person_id
        self.setWindowTitle("Edit Employee")
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.setFocus()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getPerson()

    def closeEvent(self, event):
        self.main = Main()  # you create another instance of the Main window to go back to

    def getPerson(self):
        query = "SELECT * FROM employees WHERE id=?"
        person = cursor.execute(query, (self.person_id, )).fetchone()
        number, name_text, surname_text, phone_text, email_text, img_addr, address_text = person

        self.name_entry.setText(name_text)
        self.surname_entry.setText(surname_text)
        self.phone_entry.setText(phone_text)
        self.email_entry.setText(email_text)
        self.img_add.setPixmap(QPixmap("images/{}".format(img_addr)))
        self.addr_editor.setText(address_text)

    def mainDesign(self):
        self.setStyleSheet("background-color: white; font-size: 14pt; font-family: Times New Roman; color: black;")
        ##################### Top Layout Widgets ######################
        self.title = QLabel("Edit Person")
        self.title.setStyleSheet(
            "font-size: 24pt; font-family: Arial; font-weight: bold;")  # The style sheet set for the title has preference over the ones set for the window
        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap('icons/person.png'))
        ##################### Bottom Layout Widgets ######################
        self.name_lbl = QLabel("Name: ")
        self.name_entry = QLineEdit()
        self.name_entry.setMinimumWidth(210)
        self.name_entry.setPlaceholderText("Enter Employee Name")
        self.surname_lbl = QLabel("Surname: ")
        self.surname_entry = QLineEdit()
        self.surname_entry.setMinimumWidth(210)
        self.surname_entry.setPlaceholderText("Enter Employee Surname")
        self.phone_lbl = QLabel("Phone: ")
        self.phone_entry = QLineEdit()
        self.phone_entry.setMinimumWidth(210)
        self.phone_entry.setPlaceholderText("Enter Employee Phone Number")
        self.email_lbl = QLabel("Email: ")
        self.email_entry = QLineEdit()
        self.email_entry.setMinimumWidth(210)
        self.email_entry.setPlaceholderText("Enter Employee Email")
        self.img_lbl = QLabel("Picture: ")
        self.img_btn = QPushButton("Browse")
        self.img_btn.setStyleSheet("background-color: orange;")
        self.addr_lbl = QLabel("Address: ")
        self.addr_editor = QTextEdit()
        self.add_btn = QPushButton("Update")
        self.add_btn.setStyleSheet("background-color: orange;")

    def layouts(self):
        ####################### Main Layouts #######################
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        ####################### Adding Layouts #######################
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)
        ####################### Adding Widgets to Top Layout #######################
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget(self.img_add)
        self.top_layout.addStretch()
        self.top_layout.setContentsMargins(110, 20, 10, 30)  # left, top, right, bottom
        ####################### Adding Widgets to Bottom Layout #######################
        self.bottom_layout.addRow(self.name_lbl, self.name_entry)
        self.bottom_layout.addRow(self.surname_lbl, self.surname_entry)
        self.bottom_layout.addRow(self.phone_lbl, self.phone_entry)
        self.bottom_layout.addRow(self.email_lbl, self.email_entry)
        self.bottom_layout.addRow(self.img_lbl, self.img_btn)
        self.bottom_layout.addRow(self.addr_lbl, self.addr_editor)
        self.bottom_layout.addRow("", self.add_btn)
        ####################### Main Window Layout #######################
        self.setLayout(self.main_layout)


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
