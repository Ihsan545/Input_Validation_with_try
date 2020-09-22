"""
Program: validation_with_if.py
Author: Ihsanullah Anwary
Last date modified:09/21/2020
This program the test program for test_validation_with_try..
"""
import unittest
import unittest.mock as result
from Input_Validation_with_try import input_validation


class MyTestCase(unittest.TestCase):

    def test_average(self):
        with result.patch('builtins.input', side_effect=[-95, 85, -90]):
            self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
