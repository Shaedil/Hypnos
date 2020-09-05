import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMainWindow
from PyQt5.QtGui import QFont


class WindowTest(QMainWindow):
    """
    Window class
    """
    def __init__(self):
        super(WindowTest, self).__init__()

        self.initUI()

    def initUI(self):
        """
        UI initializer
        :return:
        :rtype:
        """
        label = QtWidgets.QLabel(self)

        label.setText("hi")
        label.move(50, 50)

        btn = QPushButton("image of plus", self)
        btn.resize(btn.sizeHint())
        btn.move(100, 100)

        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Create new doc")
        self.resize(1000, 500)
        self.show()

        def onclick():
            """
            button clickes
            :return:
            :rtype:
            """
            self.label.setText("Btn clicked")


def onclick():
    """
    button clickes
    :return:
    :rtype:
    """
    print("clicked")


def main():
    """

    :return:
    :rtype:
    """
    app = QApplication(sys.argv)
    win = WindowTest()
    win.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()
