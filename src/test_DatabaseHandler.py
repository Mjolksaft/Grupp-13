import unittest
import datetime
from mysql.connector import Error

import DatabaseHandler

class TestDatabaseHandler(unittest.TestCase): 
    """DatabaseHandler tests."""

    def test_Init(self):
        """test the init class"""
    
    def test_createAccount(self):
        """test so that the user doesnt already exist"""
        dh = DatabaseHandler.DatabaseHandler()
        with self.assertRaises(Error):
            dh.createAccount("test", "test")

    def test_login(self):
        """checks so that the right exceptions gets raised when wrong inputs"""
        dh = DatabaseHandler.DatabaseHandler()
        self.assertTrue(dh.login("test", "test"))
        self.assertFalse(dh.login("wrong Name", "test"))
        self.assertFalse(dh.login("test", "wrong password"))
            

    def test_getTable(self):
        """test the getTable function"""
        dh = DatabaseHandler.DatabaseHandler()
        dh.currentUser = 17
        itemList = ['test', "10:10:10", "10:10:10"]
        dh.addSubject(itemList)
        """checks so that the correct data gets sent in the correct order"""
        res = dh.getTable()
        self.assertEqual(res[0][0], 'test')
        self.assertEqual(res[0][1], datetime.timedelta(seconds=36610))
        self.assertEqual(res[0][2], datetime.timedelta(seconds=36610))
        dh.deleteContent()

if __name__ == '__main__':
    unittest.main()
