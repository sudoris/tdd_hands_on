import unittest
from task import fizz_buzz


class TestCase(unittest.TestCase):
  
    def test1(self):
        input = 1
        expected = '1'
        self.assertEqual(fizz_buzz(input), expected)

    def test2(self):
        input = 2
        expected = '2'
        self.assertEqual(fizz_buzz(input), expected)

    def test3(self):
        input = 3
        expected = 'fizz'
        self.assertEqual(fizz_buzz(input), expected)

    def test5(self):
        input = 5
        expected = 'buzz'
        self.assertEqual(fizz_buzz(input), expected)

    def test6(self):
        input = 6
        expected = 'fizz'
        self.assertEqual(fizz_buzz(input), expected)

if __name__ == '__main__':
    unittest.main()