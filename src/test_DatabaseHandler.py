import unittest
import datetime
from mysql.connector import Error, IntegrityError

import database_handler

class TestDatabaseHandler(unittest.TestCase): 
    """DatabaseHandler tests."""

    def test_Init(self):
        """test the init class"""
        dh = database_handler.DatabaseHandler()
        self.assertEqual(dh.current_user, 'none')
    
    def test_hashPassword(self):
        """"""
        dh = database_handler.DatabaseHandler()
        dh.hash_password("password")
        password = dh.hash_password("password")
        self.assertNotEqual(password, "password")
        self.assertEqual(password, dh.hash_password("password"))

    def test_createAccount(self):
        """test so that the user doesnt already exist"""
        dh = database_handler.DatabaseHandler()
        result = dh.login("test", "test")
        self.assertTrue(result)
        dh.create_account("test", "test")

    def test_login(self):
        """checks so that the right exceptions gets raised when wrong inputs"""
        dh = database_handler.DatabaseHandler()
        self.assertTrue(dh.login("test", "test"))
        self.assertFalse(dh.login("wrong Name", "test"))
        self.assertFalse(dh.login("test", "wrong password"))
            

    def test_getTable(self):
        """test the getTable function"""
        dh = database_handler.DatabaseHandler()
        dh.current_user = 1
        itemList = ['test', "10:10:10", "10:10:10"]
        dh.add_subject(itemList)
        """checks so that the correct data gets sent in the correct order"""
        res = dh.get_table()
        self.assertEqual(res[0][0], 'test')
        self.assertEqual(res[0][1], datetime.timedelta(seconds=36610))
        self.assertEqual(res[0][2], datetime.timedelta(seconds=36610))
        dh.delete_content()

if __name__ == '__main__':
    unittest.main()
