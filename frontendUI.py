from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
import sys
import backend as be

# credit to https://www.luochang.ink/posts/pyqt5_layout_sidebar/ for the base layout
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Hypnos')

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # add all widgets
        self.btn_1 = QPushButton('Saved Files', self)
        self.btn_2 = QPushButton('Transcribe Audio', self)
        self.btn_3 = QPushButton('Generate Qs', self)
        self.btn_4 = QPushButton('save&summariize ', self)
        self.btn_5 = QPushButton('save Qs', self)

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)
        self.btn_5.clicked.connect(self.button5)

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()
        self.tab5 = self.ui5()

        self.initUI()
        self.show()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addWidget(self.btn_5)

        left_layout.addStretch(20)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 150)
        main_layout.setStretch(1, 450)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        # main_widget.setStyleSheet("background-color:#236477;");


    # -----------------
    # buttons

    def button1(self):
        self.right_widget.setCurrentIndex(0)

    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)

    def button4(self):
        self.right_widget.setCurrentIndex(3)

    def button5(self):
        self.right_widget.setCurrentIndex(4)

    # -----------------
    # pages

    def ui1(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('List of Saved Files'))

        main = QWidget()
        main.setLayout(main_layout)


        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Transcribe audio'))
        main = QWidget()
        main.setLayout(main_layout)

        uploadButton = QPushButton(self)
        uploadButton.setText("Upload audio file")
        uploadButton.clicked.connect(self.openUserFiles)
        uploadButton.setObjectName("uploadButton")


        uploadIconButton = QPushButton(self)
        # uploadButton.clicked.connect(self.openUserFiles)
        uploadIconButton.setObjectName("uploadIconButton")
        main_layout.addWidget(uploadButton, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(uploadIconButton, alignment=QtCore.Qt.AlignCenter)

        #check if file path successful
        # self.audioUploadedUI()
        return main

    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Generate Questions'))
        main = QWidget()
        main.setLayout(main_layout)

        questionGenButton = QPushButton(self)
        questionGenButton.setText("Generate practice Questions")
        questionGenButton.clicked.connect(self.questionGenerator)
        questionGenButton.setObjectName("questionGenButton")

        questionGenIconButton = QPushButton(self)
        questionGenIconButton.setObjectName("questionGenIconButton")
        main_layout.addWidget(questionGenButton, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(questionGenIconButton, alignment=QtCore.Qt.AlignCenter)

        # check if file path successful
        # self.textfileUploadedUI()
        return main

    def ui4(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Will be hidden from sidebar --> save or summarize'))
        main = QWidget()
        main.setLayout(main_layout)

        textEdit = QTextEdit(self)
        textEdit.setObjectName("textEdit")

        saveButton = QPushButton(self)
        saveButton.setText("Save")
        saveButton.clicked.connect(self.save)
        saveButton.setObjectName("saveButton")

        saveIconButton = QPushButton(self)
        saveIconButton.setObjectName("saveIconButton")


        summarizeButton = QPushButton(self)
        summarizeButton.setText("Generate Summary")
        summarizeButton.clicked.connect(self.summarizeText)
        summarizeButton.setObjectName("summarizeButton")

        summarizeIconButton = QPushButton(self)
        # summarizeButton.clicked.connect(self.summarizeText)
        summarizeIconButton.setObjectName("summarizeIconButton")

        main_layout.addWidget(textEdit, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(saveButton, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(saveIconButton, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(summarizeButton, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(summarizeIconButton, alignment=QtCore.Qt.AlignCenter)

        return main


    def ui5(self):
        #once a valid text file path has bee recorded --> thhis ui should show up
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Will be hidden from sidebar --> save or summarize'))
        main = QWidget()
        main.setLayout(main_layout)

        textEdit = QTextEdit(self)
        textEdit.setObjectName("textEdit")

        saveButton = QPushButton(self)
        saveButton.setText("Save")
        saveButton.clicked.connect(self.save)
        saveButton.setObjectName("saveButton")
        saveIconButton = QPushButton(self)
        saveIconButton.setObjectName("saveIconButton")

        main_layout.addWidget(textEdit, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(saveButton, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(saveIconButton, alignment=QtCore.Qt.AlignCenter)
        return main



#linkingbackend to frontend

    def openUserFiles(self) -> True:
        #opening the file dialog for selecting the file
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Video Files(*.wav)")
        print(fname[0])
        if fname[0] != '':
            self.script, self.pscript = be.backend(fname[0])
            self.summ = be.sumThis(self.pscript)
            self.questions, self.keywords = be.genQ(self.script, self.pscript)
            return True
        self.textEdit.setText(script)
    #fname[0] is the absolute file path
        #connection to the backend happens here

    def save(self):
        fname=QFileDialog.getSaveFileName(self,'Save File')
        data=self.textEdit.toPlainText()
        file=open(fname[0],'w')
        file.write(data)
        file.close()
        print("your text has saved to drive")

    def summarizeText(self):
        self.textEdit.setText(self.summ)

        print("your text has been summarize")

    def questionGenerator(self):
        self.textEdit.setText(self.questions)
        print("you have generated practice questions")

    # def audioUploadedUI(self):
    #     #once a valid audio file path has bee recorded --> thhis ui should show up
    #     main_layout = QVBoxLayout()
    #     main_layout.addStretch(5)
    #     main = QWidget()
    #     main.setLayout(main_layout)
    #
    #     textEdit = QTextEdit(self)
    #     textEdit.setGeometry(QtCore.QRect(90, 10, 591, 361))
    #     textEdit.setObjectName("textEdit")
    #
    #     saveButton = QPushButton(self)
    #     saveButton.setText("Save")
    #     saveButton.setGeometry(200, 450, 100, 100)
    #     saveButton.resize(400, 100)
    #     saveButton.clicked.connect(self.save)
    #     saveButton.setObjectName("saveButton")
    #
    #     saveIconButton = QPushButton(self)
    #     saveIconButton.setGeometry(50, 450, 100, 100)
    #
    #
    #     summarizeButton = QPushButton(self)
    #     summarizeButton.setText("Generate Summary")
    #     summarizeButton.setGeometry(200, 300, 100, 100)
    #     summarizeButton.resize(400, 100)
    #     summarizeButton.clicked.connect(self.summarizeText)
    #     summarizeButton.setObjectName("summarizeButton")
    #
    #     summarizeIconButton = QPushButton(self)
    #     summarizeIconButton.setGeometry(50, 300, 100, 100)
    #     # summarizeButton.clicked.connect(self.summarizeText)
    #     summarizeIconButton.setObjectName("summarizeIconButton")
    #
    #     main_layout.addWidget(textEdit)
    #     main_layout.addWidget(saveButton)
    #     main_layout.addWidget(saveIconButton)
    #     main_layout.addWidget(summarizeButton)
    #     main_layout.addWidget(summarizeIconButton)
    #     return main
    #
    # def fileUploadedUI(self):
    #     #once a valid text file path has bee recorded --> thhis ui should show up
    #     main_layout = QVBoxLayout()
    #     main_layout.addStretch(5)
    #     main = QWidget()
    #     main.setLayout(main_layout)
    #
    #     textEdit = QTextEdit(self)
    #     textEdit.setGeometry(QtCore.QRect(90, 10, 591, 361))
    #     textEdit.setObjectName("textEdit")
    #
    #     saveButton = QPushButton(self)
    #     saveButton.setText("Save")
    #     saveButton.setGeometry(200, 450, 100, 100)
    #     saveButton.resize(400, 100)
    #     saveButton.clicked.connect(self.save)
    #     saveButton.setObjectName("saveButton")
    #
    #     saveIconButton = QPushButton(self)
    #     saveIconButton.setGeometry(50, 450, 100, 100)
    #
    #     main_layout.addWidget(textEdit)
    #     main_layout.addWidget(saveButton)
    #     main_layout.addWidget(saveIconButton)
    #     return main

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # app.setStyle('Fusion')
    window = Window()
    window.stylesheet = """
    QPushButton{
        background-color: #173042;
        color: #fff;
        border-radius: 10px;
        font-size: 25px;
        font-family: 'Roboto';
        font-weight: 3000; 
    }
        
    QHBoxLayout {
        background-color: #236477;

    }
    
    QVBoxLayout {
        background-color: #236477;

    }
    QPushButton#uploadIconButton {
        background-color: #31BE8B;
        background-image: url(images/icon (2).png);
        border-radius: 50px;
        background-repeat: repeat;
        background-attachment: fixed;
        background-position: center;
        }
        
        
    QPushButton#saveIconButton {
        background-color: #31BE8B;
        background-image: url(images/icon (3).png);
        border-radius: 50px;
        background-repeat: repeat;
        background-attachment: fixed;
        background-position: center;
        }
        
    QPushButton#summarizeIconButton, QPushButton#questionGenIconButton{
        background-color: #31BE8B;
        background-image: url(images/icon (1).png);
        border-radius: 50px;
        background-repeat: repeat;
        background-attachment: fixed;
        background-position: center;
        }
    """
    app.setStyleSheet(window.stylesheet)
    sys.exit(app.exec_())
