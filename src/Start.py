from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import sys

import DatabaseHandler
import main

class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.dh = DatabaseHandler.DatabaseHandler()
        uic.loadUi('Start.ui', self)
        self.setWindowTitle('Start')
        self.Login.clicked.connect(self.login)

    def login(self):
        main.widget.setCurrentIndex(main.widget.currentIndex()+1)