import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Window(QMainWindow): # it is important to inherit from QMainWindow
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 600, 600)
        self.setWindowTitle("Toolbar Widget")
        self.UI()

    def UI(self):
        #################### Main Menu ####################
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file = menu_bar.addMenu("File")
        edit = menu_bar.addMenu("Edit")
        code = menu_bar.addMenu("Code")
        help_ = menu_bar.addMenu("Help")

        #################### Sub Menu Items ####################
        new = QAction("New Project", self)
        new.setShortcut("Ctrl+0")
        file.addAction(new)

        open_ = QAction("Open", self)
        file.addAction(open_)

        exit = QAction("Exit", self)
        exit.setIcon(QIcon("icons/exit.png"))
        exit.triggered.connect(self.exitFunc)
        file.addAction(exit)

        ##################### Tool Bar #########################
        tb = self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        newTb = QAction(QIcon("icons/folder.png"), "New", self)
        tb.addAction(newTb)

        openTb = QAction(QIcon("icons/empty.png"), "Open", self)
        tb.addAction(openTb)

        saveTb = QAction(QIcon("icons/save.png"), "Save", self)
        tb.addAction(saveTb)

        exitTb = QAction(QIcon("icons/exit.png"), "Exit", self)
        exitTb.triggered.connect(self.exitFunc)
        tb.addAction(exitTb)

        tb.actionTriggered.connect(self.btnFunc)

        combo = QComboBox()
        combo.addItems(["Orange", "Banana", "Apple"])
        tb.addWidget(combo)

        self.show()

    def exitFunc(self):
        mbox = QMessageBox.information(self, "Warning", "Are you sure to exit?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()

    def btnFunc(self, btn):
        if btn.text() == "New":
            print("You clicked New button")
        elif btn.text() == "Open":
            print("You clicked Open button")
        else:
            print("You clicked Save button")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()