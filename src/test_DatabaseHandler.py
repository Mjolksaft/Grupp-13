import unittest
import DatabaseHandler

class TestDatabaseHandler(unittest.TestCase): 
    """DatabaseHandler tests."""
    def test_createAccount(self):
        """test so that the user doesnt already exist"""
        dh = DatabaseHandler.DatabaseHandler
        self.mock.patch()

if __name__ == '__main__':
    unittest.main()
    