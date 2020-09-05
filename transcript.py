from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Transcript")
        self.resize(800,600)

        self.text_edit()

        self.save_button()

        self.summarize_button()

        self.show()


    def text_edit(self):
        #function for defining textedit
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(90, 10, 591, 361))
        self.textEdit.setObjectName("textEdit")

    def save_button(self):
        #function for defining save push button 
        self.saveButton = QtWidgets.QPushButton("Save",self)
        self.saveButton.setGeometry(QtCore.QRect(260, 380, 221, 61))
        self.saveButton.clicked.connect(self.save)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setAutoFillBackground(True)
        self.saveButton.setStyleSheet("background-color=blurgb(85, 170, 255)e;\n"
"border-style=outset;\n"
"border-width=2px;\n"
"border-radius=10px;\n"
"border-color=blue;")

    def summarize_button(self):
        #function for definning summarizebutton
        self.summarizeButton = QtWidgets.QPushButton("Summarize",self)
        self.summarizeButton.setGeometry(QtCore.QRect(260, 460, 221, 61))
        self.summarizeButton.setObjectName("summarizeButton")
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.summarizeButton.setFont(font)

    def save(self):
        #function for saving the text in textfield
        fname=QtWidgets.QFileDialog.getSaveFileName(self,'Save File')
        data=self.textEdit.toPlainText()
        if fname[0]:
            file=open(fname[0],'w')
            file.write(data)
            file.close()
app=QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window=Ui_MainWindow()
sys.exit(app.exec_())
