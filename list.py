import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)  # (loc_x, loc_y, size_x, size_y)
        self.setWindowTitle("Using Timer")
        self.UI()

    def UI(self):
        self.add_record = QLineEdit(self)
        self.add_record.move(100, 50)
        self.list_widget = QListWidget(self)
        self.list_widget.move(100, 80)

        # Add some items to the list widget
        list1 = ["apple", "banana", "watermelon"]
        self.list_widget.addItems(list1)
        [self.list_widget.addItem(str(number)) for number in range(5, 11)]

        ############## Buttons ################

        btn_add = QPushButton("Add", self)
        btn_add.move(360, 80)
        btn_add.clicked.connect(self.func_add)

        btn_delete = QPushButton("Delete", self)
        btn_delete.move(360, 110)
        btn_delete.clicked.connect(self.func_delete)

        btn_get = QPushButton("Get", self)
        btn_get.move(360, 140)
        btn_get.clicked.connect(self.func_get)

        btn_del_all = QPushButton("Delete All", self)
        btn_del_all.move(360, 170)
        btn_del_all.clicked.connect(self.func_del_all)

        self.show()

    def func_add(self):
        value = self.add_record.text()
        self.list_widget.addItem(value)
        self.add_record.setText("")

    def func_delete(self):
        id = self.list_widget.currentRow()
        self.list_widget.takeItem(id)

    def func_get(self):
        value = self.list_widget.currentItem().text()
        print(value)

    def func_del_all(self):
        self.list_widget.clear()

def main():
    App = QApplication(sys.argv)
    window = Window()
    # window.start()  # You can also start your timer as soon as you start your application
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()