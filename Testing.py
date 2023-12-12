import unittest
from functions import PmCc
from variables import video_gamer, gamingtwelve_rate, data_dates, violent_crimes, sexual_offences, weapon_possession,suicide_rate,homicide_rate

x = video_gamer
y = violent_crimes

class TestFunction1(unittest.TestCase):

    def test_addition_lower_one(self):
            result = PmCc(x, y)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one(self):
            result = PmCc(x, y)
            self.assertGreaterEqual(abs(result), 0.1)

y = sexual_offences

class TestFunction2(unittest.TestCase):

    def test_addition_lower_one(self):
            result = PmCc(x, y)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one(self):
            result = PmCc(x, y)
            self.assertGreaterEqual(abs(result), 0.1)

y = weapon_possession

class TestFunction3(unittest.TestCase):

    def test_addition_lower_one(self):
            result = PmCc(x, y)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one(self):
            result = PmCc(x, y)
            self.assertGreaterEqual(abs(result), 0.1)

y = suicide_rate

class TestFunction4(unittest.TestCase):

    def test_addition_lower_one(self):
            result = PmCc(x, y)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one(self):
            result = PmCc(x, y)
            self.assertGreaterEqual(abs(result), 0.1)

x = gamingtwelve_rate
y = homicide_rate

class TestFunction5(unittest.TestCase):

    def test_addition_lower_one(self):
            result = PmCc(x, y)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one(self):
            result = PmCc(x, y)
            self.assertGreaterEqual(abs(result), 0.1)


if __name__ == '__main__':
    unittest.main()