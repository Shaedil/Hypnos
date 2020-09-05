import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# WHITE=QtGui.QColor(255,255,255)

class Hypnos:
    def __init__(self):
        # super().__init__()
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()

        self.window.stylesheet = """
            QPushButton{
                background-color: #173042;
                color: #fff;
                border-radius: 10px;
                font-size: 25px;
                font-family: 'Roboto';
                font-weight: 3000;
            }
            
        
            QPushButton#summarizeIconButton, QPushButton#questionGenIconButton{
                background-color: #31BE8B;
                background-image: url(images/icon (1).png);
                border-radius: 50px;
                background-repeat: repeat;
                background-attachment: fixed;
                background-position: center;
            }
            
            QPushButton#uploadIconButton{
                background-color: #31BE8B;
                background-image: url(images/icon (2).png);
                border-radius: 50px;
                background-repeat: repeat;
                background-attachment: fixed;
                background-position: center;
            }
            QPushButton#saveIconButton{
                background-color: #31BE8B;
                background-image: url(images/icon (3).png);
                border-radius: 50px;
                background-repeat: repeat;
                background-attachment: fixed;
                background-position: center;
            }
            """

        self.UiComponents()

        # setting the window title
        self.window.setWindowTitle("Hypnos")
        # sizing the mainWindow
        self.window.setGeometry(1000, 1000, 1000, 1000)
        self.window.show()
        self.app.setStyleSheet(self.window.stylesheet)
        sys.exit(self.app.exec_())

        # method for widgets
    def UiComponents(self):

        uploadButton = QPushButton(self.window)
        uploadButton.setText("Upload audio file")
        uploadButton.setGeometry(200, 150, 100, 100)
        uploadButton.resize(400, 100)
        uploadButton.clicked.connect(self.openUserFiles)
        uploadButton.setObjectName("uploadButton")

        uploadIconButton = QPushButton(self.window)
        uploadIconButton.setGeometry(50, 150, 100, 100)
        # uploadButton.clicked.connect(self.openUserFiles)
        uploadIconButton.setObjectName("uploadIconButton")

        summarizeButton = QPushButton(self.window)
        summarizeButton.setText("Generate Summary")
        summarizeButton.setGeometry(200, 300, 100, 100)
        summarizeButton.resize(400, 100)
        summarizeButton.clicked.connect(self.summarizeText)
        summarizeButton.setObjectName("summarizeButton")

        summarizeIconButton = QPushButton(self.window)
        summarizeIconButton.setGeometry(50, 300, 100, 100)
        # summarizeButton.clicked.connect(self.summarizeText)
        summarizeIconButton.setObjectName("summarizeIconButton")

        saveButton = QPushButton(self.window)
        saveButton.setText("Save")
        saveButton.setGeometry(200, 450, 100, 100)
        saveButton.resize(400, 100)
        saveButton.clicked.connect(self.save)
        saveButton.setObjectName("saveButton")

        saveIconButton = QPushButton(self.window)
        saveIconButton.setGeometry(50, 450, 100, 100)
        # saveButton.clicked.connect(self.save)
        saveIconButton.setObjectName("saveIconButton")

        questionGenButton = QPushButton(self.window)
        questionGenButton.setText("Generate practice Questions")
        questionGenButton.setGeometry(200, 600, 100, 100)
        questionGenButton.resize(400, 100)
        questionGenButton.clicked.connect(self.questionGenerator)
        questionGenButton.setObjectName("questionGenButton")

        questionGenIconButton = QPushButton(self.window)
        questionGenIconButton.setGeometry(50, 600, 100, 100)
        # questionGenButton.clicked.connect(self.questionGenerator)
        questionGenIconButton.setObjectName("questionGenIconButton")

    def questionGenerator(self):
        print("you have generated practive questions")

    def save(self):
        print("your text has saved to drive")

    def summarizeText(self):
        print("your text has been summarize")

    def openUserFiles(self):
        #opening the file dialog for selecting the file
        fname = QFileDialog.getOpenFileName(self.window, 'Open File', 'c:\\', "Video Files(*.mp4)")
        print(fname[0]) #fname[0] is the absolute file path
        #connection to the backend happens here


if __name__ == "__main__":
    main = Hypnos()
