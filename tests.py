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

    def test3(self):
        pwd = '1234567'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test4(self):
        pwd = '123456789abcdefghijklmnopqrsabcdefgaeiou'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test5(self):
        pwd = '123456789'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test6(self):
        pwd = 'abcdefghijkl'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test7(self):
        pwd = 'AB1235FEAFEA'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)
    
    def test8(self):
        pwd = 'ab1235feafea'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)

    def test9(self):
        pwd = 'ab1235FEA'
        expected = False
        self.assertEqual(check_pwd(pwd), expected)
    
    def test10(self):
        pwd = '1abc1$35FEA'
        expected = True
        self.assertEqual(check_pwd(pwd), expected)


if __name__ == '__main__':
    unittest.main()