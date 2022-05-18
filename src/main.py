"""
Welcome to the project!.
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import sys

import DatabaseHandler

class Start(QWidget):
    def __init__(self, dh):
        super().__init__()
        self.dh = dh
        uic.loadUi('Start.ui', self)
        self.setWindowTitle('Start')
        self.Login.clicked.connect(self.login)

    def login(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class Login(QWidget):
    def __init__(self, dh):
        super().__init__()
        self.dh = dh
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
            self.Password.clear()
            self.Username.clear()
        else:
            self.error.setText("input fields cannot be empty")

    def login(self):
        """Allows the user to login to a specific account."""
        userName = self.Username_2.text()
        password = self.Password_2.text()
        if userName != "" and password != "":
            succes = self.dh.login(userName, password)
            if succes == True:
                print("succes")
                widget.setCurrentIndex(2)
            else:
                print("failed")
        else:
            self.error.setText("input fields cannot be empty")

class Home(QWidget):
    """the home screen which holds the users schedule"""
    def __init__(self, dh):
        self.dh = dh
        super().__init__()
        uic.loadUi('Home.ui', self)
        self.Table.setColumnWidth(0,191)
        self.Table.setColumnWidth(1,191)
        self.setWindowTitle('Home')
        self.BUTTON.clicked.connect(self.setTable)
        self.addContent.clicked.connect(self.setData)
        self.newRowButton.clicked.connect(self.newRow)
        self.deleteButton.clicked.connect(self.deleteRow)
        self.saveButton.clicked.connect(self.save)

    def setTable(self):
        """gets the table contet for the correct user"""
        res = self.dh.getTable()
        self.Table.setRowCount(len(res))
        print(res)
        for row in range(self.Table.rowCount()):
            for column in range(self.Table.columnCount()):
                self.Table.setItem(row, column, QtWidgets.QTableWidgetItem(str(res[row][column])))
    
    # def getTableContent(self, row, column):
    #     """gets the data from the table"""
    #     item = self.Table.item(0,0)
    #     print(item.text)

    def setData(self):
        """sets the data in the mysql database"""
        subject = self.Subject.text()
        time = self.Time.text()
        if subject != "" and time != "":
            self.dh.addSubject(subject, time)
            self.Subject.clear()
            self.Time.clear()
    
    def newRow(self):
        """adds a new row to the table."""
        currentRow = self.Table.currentRow()
        self.Table.insertRow(currentRow+1)

    def deleteRow(self):
        """deletes the row from the table"""
        if self.Table.rowCount() > 0:
            currentRow = self.Table.currentRow()
            self.Table.removeRow(currentRow)

    def save(self):
        """saves to the database"""
        self.dh.deleteContent()
        contentList = []
        for row in range(self.Table.rowCount()):
            rowList = []
            for column in range(self.Table.columnCount()):
                widgetItem = self.Table.item(row, column)
                rowData = widgetItem.text()
                rowList.append(rowData)
            contentList.append(rowList)

        for item in contentList:
            self.dh.addSubject(item)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    dh = DatabaseHandler.DatabaseHandler()
    
    startScreen = Start(dh)
    loginScreen = Login(dh)
    homeScreen = Home(dh)
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(startScreen)
    widget.addWidget(loginScreen)
    widget.addWidget(homeScreen)
    widget.setFixedHeight(500)
    widget.setFixedWidth(800)
    widget.show()

    try:
        sys.exit(app.exec_())
    except SystemError as error:
        print(error)
