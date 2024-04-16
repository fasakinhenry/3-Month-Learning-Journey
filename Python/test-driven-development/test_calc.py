#!/usr/bin/python3
import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(calc.add(10, 5), 15)
        self.asserEqual(calc.add(-1, 1), 0)
        srlf.assertEqual(calc.add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
