import unittest
from functions import PmCc

class TestFunction1(unittest.TestCase):

    def test_addition_lower_one(self):
            result = PmCc(x, y)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one(self):
            result = PmCc(x, y)
            self.assertGreaterEqual(abs(result), 0.1)


if __name__ == '__main__':
    unittest.main()