import unittest
from functions import PmCc
from variables import video_gamer, gamingtwelve_rate, data_dates, violent_crimes, sexual_offences, weapon_possession,suicide_rate,homicide_rate

class TestFunction1(unittest.TestCase):

    def test_addition_lower_one1(self):
            result = PmCc(video_gamer, violent_crimes)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one1(self):
            result = PmCc(video_gamer, violent_crimes)
            self.assertGreaterEqual(abs(result), 0.1)

    def test_addition_lower_one2(self):
            result = PmCc(video_gamer, sexual_offences)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one2(self):
            result = PmCc(video_gamer, sexual_offences)
            self.assertGreaterEqual(abs(result), 0.1)


    def test_addition_lower_one3(self):
            result = PmCc(video_gamer, weapon_possession)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one3(self):
            result = PmCc(video_gamer, weapon_possession)
            self.assertGreaterEqual(abs(result), 0.1)


    def test_addition_lower_one4(self):
            result = PmCc(video_gamer, suicide_rate)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one4(self):
            result = PmCc(video_gamer, suicide_rate)
            self.assertGreaterEqual(abs(result), 0.1)


    def test_addition_lower_one5(self):
            result = PmCc(gamingtwelve_rate, homicide_rate)
            self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one5(self):
            result = PmCc(gamingtwelve_rate, homicide_rate)
            self.assertGreaterEqual(abs(result), 0.1)


if __name__ == '__main__':
    unittest.main()