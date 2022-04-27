from mimetypes import init
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Test.ui', self)
        self.setWindowTitle('My App')
        self.button.clicked.connect(self.sayHello)
        

    def sayHello(self):
        inputText = self.input.text()
        self.output.setText('hello {0}'.format(inputText))
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    
    myApp = window()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemError as error:
        print(error)