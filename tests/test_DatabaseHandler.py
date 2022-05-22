import unittest
from unittest.mock import Mock
from src import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase): 
    """DatabaseHandler tests."""
    mock = Mock()
    print(mock)
    def test_createAccount(self):
        """test so that the user doesnt already exist"""
        
        

if __name__ == '__main__':
    unittest.main()
