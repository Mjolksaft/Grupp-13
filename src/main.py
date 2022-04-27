"""
Welcome to the project!.

"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import sys

import DatabaseHandler

class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.dh = DatabaseHandler.DatabaseHandler()
        uic.loadUi('Start.ui', self)
        self.setWindowTitle('Start')
        self.Login.clicked.connect(self.login)
    
    def login(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.dh = DatabaseHandler.DatabaseHandler()
        uic.loadUi('Login.ui', self)
        self.setWindowTitle('Login/register')
        self.Button.clicked.connect(self.createAccount)
        self.Button_2.clicked.connect(self.login)
        self.back.clicked.connect(self.Back)

    def Back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    
    def createAccount(self):
        """Allows the user to create a account with name and password."""
        userName = self.Username.text()
        password = self.Password.text()
        if userName != "" and password != "":
            self.dh.createAccount(userName, password)

    def login(self):
        """Allows the user to login to a specific account."""
        userName = self.Username_2.text()
        password = self.Password_2.text()
        self.dh.login(userName, password)

if __name__ == "__main__":
    app = QApplication(sys.argv) 

    startScreen = Start()
    loginScreen = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(startScreen)
    widget.addWidget(loginScreen)
    widget.setFixedHeight(500)
    widget.setFixedWidth(800)
    widget.show()
    
    try:
        sys.exit(app.exec_())
    except SystemError as error:
        print(error)
