import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        pwd = '1'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)
    
    def test2(self):
        pwd = ''
        expected = False
        self.assertEqual(check_pwd(pwd), expected)
    

if __name__ == '__main__':
    unittest.main()