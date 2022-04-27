from tokenize import String
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget

import DatabaseHandler

class gui(QWidget):
    def __init__(self):
        super().__init__()
        self.dh = DatabaseHandler.DatabaseHandler()
        uic.loadUi('Test.ui', self)
        self.setWindowTitle('My App')
        self.Button.clicked.connect(self.createAccount)
        self.Button_2.clicked.connect(self.login)

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