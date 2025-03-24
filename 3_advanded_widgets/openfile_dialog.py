import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 400, 400)
        self.setWindowTitle("File Dialogs")
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        file_btn = QPushButton("Open File")
        file_btn.clicked.connect(self.openFile)
        font_btn = QPushButton("Chenge Font")
        font_btn.clicked.connect(self.changeFont)
        color_btn = QPushButton("Change color")
        color_btn.clicked.connect(self.changeColor)

        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(file_btn)
        hbox.addWidget(font_btn)
        hbox.addWidget(color_btn)
        hbox.addStretch()

        self.setLayout(vbox)

        self.show()

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(font)

    def changeColor(self):
        color= QColorDialog.getColor()
        self.editor.setTextColor(color)

    def openFile(self):
        url = QFileDialog.getOpenFileName(self, "Open a file", "", "All Files(*);;txt")
        print(url[0])
        fileUrl = url[0]

        file = open(fileUrl, 'r')
        content = file.read()
        self.editor.setText(content)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()