"""
Welcome to the project!.

"""

from PyQt5.QtWidgets import QApplication
import sys
import gui

if __name__ == "__main__":
    app = QApplication(sys.argv) 

    myApp = gui.Start()
    myApp.show()
    
    try:
        sys.exit(app.exec_())
    except SystemError as error:
        print(error)
