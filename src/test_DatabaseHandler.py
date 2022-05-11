import unittest

import DatabaseHandler
from mysql.connector import connect, Error

class TestDatabaseHandler(unittest.TestCase): 
    """DatabaseHandler tests."""
    def test_createAccount(self):
        dh = DatabaseHandler.DatabaseHandler()
        # self.assertRaises(Error, dh.createAccount("test","test"))

    def test_login(self):
        """checks if it returns true if the user test can login with password test"""
        dh = DatabaseHandler.DatabaseHandler()
        success = dh.login("test", "test")
        self.assertTrue(success)
        failure = dh.login("test", "test2")
        self.assertFalse(failure)

if __name__ == '__main__':
    unittest.main()
    