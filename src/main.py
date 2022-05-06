"""
Welcome to the project!.
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import sys
import os
import hashlib

import DatabaseHandler



def sha256_hash_password(password, salt):
    pepper = "(!/¤()!/¤(aoiidaipsmd)(!(¤=)!())jnaisjdniJANISNDiasnd"
    return hashlib.sha256((password + pepper + salt).encode("utf-8")).hexdigest()

def verify_password(password, salt, hashed_password):
    pepper = "(!/¤()!/¤(aoiidaipsmd)(!(¤=)!())jnaisjdniJANISNDiasnd"
    return sha256_hash_password(password, salt) == hashed_password

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
        salt = (str)(os.urandom(16))
        password = sha256_hash_password(self.Password.text(), salt)
        if userName != "" and password != "":
            self.dh.createAccount(userName, password, salt)
        else:
            self.error.setText("input fields cannot be empty")

    def login(self):
        """Allows the user to login to a specific account."""
        userName = self.Username_2.text()
        password = self.Password_2.text()
        if userName != "" and password != "":
            widget.setCurrentIndex(widget.currentIndex()+1)
            # self.dh.login(userName, password)
            if verify_password(password, self.dh.getSalt(userName), self.dh.getPassword(userName)):
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.error.setText("Wrong username or password")
        else:
            self.error.setText("input fields cannot be empty")

class Calendar(QWidget):
    def __init__(self):
        super().__init__()
        self.dh = DatabaseHandler.DatabaseHandler()
        uic.loadUi('Calendar.ui', self)
        self.setWindowTitle('Calendar')


if __name__ == "__main__":
    app = QApplication(sys.argv) 

    startScreen = Start()
    loginScreen = Login()
    calendarScreen = Calendar()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(startScreen)
    widget.addWidget(loginScreen)
    widget.addWidget(calendarScreen)
    widget.setFixedHeight(500)
    widget.setFixedWidth(800)
    widget.show()

    try:
        sys.exit(app.exec_())
    except SystemError as error:
        print(error)
