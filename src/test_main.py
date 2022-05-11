from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import sys

import unittest
import main

class test_start(unittest.TestCase):
    """"""
    def test_StartLogin(self):
        """checks so it switches to the correct window"""
        start = main.Start()
        start.login()


if __name__ == '__main__':
    unittest.main()
