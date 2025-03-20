import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 400, 400)
        self.setWindowTitle("Form Layout")
        self.UI()

    def UI(self):
        form = QFormLayout()
        # form.setRowWrapPolicy(QFormLayout.WrapAllRows)  # A policy can change how it is displayed

        name_txt = QLabel("Name:")
        name_input = QLineEdit()
        pass_txt = QLabel("Password:")
        pass_input = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(QLineEdit())
        hbox_1.addWidget(QLineEdit())

        # You can only add two widgets to your row, but you can add more by putting the widgets in a box
        form.addRow(name_txt, hbox_1)
        form.addRow(pass_txt, pass_input)
        form.addRow(QLabel("Country"), QComboBox())
        form.addRow(hbox)

        self.setLayout(form)

        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()