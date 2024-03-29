# Importing required libraries and functions for the test
import unittest
from functions import PmCc
import numpy as np
import pandas as pd

# Function to convert a pandas dataframe to a dictionary for easier data manipulation
def dataframe_to_dictionary(df):
    dictionary = {}
    for header in df:
        dictionary[header] = [data for data in df[header]]
    return dictionary

# Unit test class inheriting from unittest.TestCase
class TestFunction1(unittest.TestCase):

 # Test case to check if the Pearson correlation coefficient is less than or equal to 1
    def test_addition_lower_one1(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id300521_uk-gaming-reach-2007-2021.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        video_gamer1 = y["Gamers"]

        video_gamer = np.array(video_gamer1)

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("statistic_id288256_number-of-violent-crime-offences-in-england-and-wales-2007-2022.xlsx", "Data", header = 3)
        df.head()

        x = dataframe_to_dictionary(df)
        violent_crimes1 = x["Crimes"]

        violent_crimes = np.array(violent_crimes1)

        # Calculate the Pearson correlation coefficient and assert it's less than or equal to 1
        result = PmCc(video_gamer, violent_crimes)
        self.assertLessEqual(abs(result), 1)

    # Test case to check if the Pearson correlation coefficient is greater than or equal to 0.1
    def test_addition_greater_point_one1(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id300521_uk-gaming-reach-2007-2021.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        video_gamer1 = y["Gamers"]

        video_gamer = np.array(video_gamer1)

        z = dataframe_to_dictionary(df)
        data_dates1 = z["UK gaming reach 2007-2021"]

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("statistic_id288256_number-of-violent-crime-offences-in-england-and-wales-2007-2022.xlsx", "Data", header = 3)
        df.head()

        x = dataframe_to_dictionary(df)
        violent_crimes1 = x["Crimes"]

        violent_crimes = np.array(violent_crimes1)

        # Calculate the Pearson correlation coefficient and assert it's greater than or equal to 0.1
        result = PmCc(video_gamer, violent_crimes)
        self.assertGreaterEqual(abs(result), 0.1)

    # Test case to check if the Pearson correlation coefficient is less than or equal to 1
    def test_addition_lower_one2(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id300521_uk-gaming-reach-2007-2021.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        video_gamer1 = y["Gamers"]

        video_gamer = np.array(video_gamer1)

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("Figure_10__Suspects_convicted_of_homicide_show_a_younger_age_profile (2).xlsx", "Data5", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        sexual_offences1 = y["Sexual Offences"]

        sexual_offences = np.array(sexual_offences1)

        # Calculate the Pearson correlation coefficient and assert it's less than or equal to 1
        result = PmCc(video_gamer, sexual_offences)
        self.assertLessEqual(abs(result), 1)

    # Test case to check if the Pearson correlation coefficient is greater than or equal to 0.1
    def test_addition_greater_point_one2(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id300521_uk-gaming-reach-2007-2021.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        video_gamer1 = y["Gamers"]

        video_gamer = np.array(video_gamer1)

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("Figure_10__Suspects_convicted_of_homicide_show_a_younger_age_profile (2).xlsx", "Data5", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        sexual_offences1 = y["Sexual Offences"]

        sexual_offences = np.array(sexual_offences1)

        # Calculate the Pearson correlation coefficient and assert it's greater than or equal to 0.1
        result = PmCc(video_gamer, sexual_offences)
        self.assertGreaterEqual(abs(result), 0.1)

    # Test case to check if the Pearson correlation coefficient is less than or equal to 1
    def test_addition_lower_one3(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id300521_uk-gaming-reach-2007-2021.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        video_gamer1 = y["Gamers"]

        video_gamer = np.array(video_gamer1)

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("statistic_id828895_number-of-possession-of-weapon.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        weapon_possession1 = y["weapon possession"]

        weapon_possession = np.array(weapon_possession1)

        # Calculate the Pearson correlation coefficient and assert it's less than or equal to 1
        result = PmCc(video_gamer, weapon_possession)
        self.assertLessEqual(abs(result), 1)

    # Test case to check if the Pearson correlation coefficient is greater than or equal to 0.1
    def test_addition_greater_point_one3(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id300521_uk-gaming-reach-2007-2021.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        video_gamer1 = y["Gamers"]

        video_gamer = np.array(video_gamer1)

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("statistic_id828895_number-of-possession-of-weapon.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        weapon_possession1 = y["weapon possession"]

        weapon_possession = np.array(weapon_possession1)

        # Calculate the Pearson correlation coefficient and assert it's greater than or equal to 0.1
        result = PmCc(video_gamer, weapon_possession)
        self.assertGreaterEqual(abs(result), 0.1)

    # Test case to check if the Pearson correlation coefficient is less than or equal to 1
    def test_addition_lower_one4(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id300521_uk-gaming-reach-2007-2021.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        video_gamer1 = y["Gamers"]

        video_gamer = np.array(video_gamer1)

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("statistic_id282160_suicide-rate-in-england-and-wales-2000-2021 (1).xlsx", "Data", header = 3)
        df.head()

        y = dataframe_to_dictionary(df)
        suicide_rate1 = y["Suicide rate "]

        suicide_rate = np.array(suicide_rate1)

        # Calculate the Pearson correlation coefficient and assert it's less than or equal to 1
        result = PmCc(video_gamer, suicide_rate)
        self.assertLessEqual(abs(result), 1)

    # Test case to check if the Pearson correlation coefficient is greater than or equal to 0.1
    def test_addition_greater_point_one4(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id300521_uk-gaming-reach-2007-2021.xlsx", "Data", header = 2)
        df.head()

        y = dataframe_to_dictionary(df)
        video_gamer1 = y["Gamers"]

        video_gamer = np.array(video_gamer1)

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("statistic_id282160_suicide-rate-in-england-and-wales-2000-2021 (1).xlsx", "Data", header = 3)
        df.head()

        y = dataframe_to_dictionary(df)
        suicide_rate1 = y["Suicide rate "]

        suicide_rate = np.array(suicide_rate1)

        # Calculate the Pearson correlation coefficient and assert it's greater than or equal to 0.1
        result = PmCc(video_gamer, suicide_rate)
        self.assertGreaterEqual(abs(result), 0.1)

    # Test case to check if the Pearson correlation coefficient is less than or equal to 1
    def test_addition_lower_one5(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id283093_number-of-homicides-in-england-and-wales-2002-2022.xlsx", "Data2", header = 2)
        df.head()

        z = dataframe_to_dictionary(df)
        gamingtwelve_rate1 = z["Games"]

        gamingtwelve_rate = np.array(gamingtwelve_rate1)

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("statistic_id283093_number-of-homicides-in-england-and-wales-2002-2022.xlsx", "Data", header = 1)
        df.head()

        z = dataframe_to_dictionary(df)
        homicide_rate1 = z["Number of homicides in England and Wales 2002-2022"]

        homicide_rate = np.array(homicide_rate1)

        # Calculate the Pearson correlation coefficient and assert it's less than or equal to 1
        result = PmCc(gamingtwelve_rate, homicide_rate)
        self.assertLessEqual(abs(result), 1)

    # Test case to check if the Pearson correlation coefficient is greater than or equal to 0.1
    def test_addition_greater_point_one5(self):

        # Load data from an excel file and convert it to a dictionary
        df = pd.read_excel("statistic_id283093_number-of-homicides-in-england-and-wales-2002-2022.xlsx", "Data2", header = 2)
        df.head()

        z = dataframe_to_dictionary(df)
        gamingtwelve_rate1 = z["Games"]

        gamingtwelve_rate = np.array(gamingtwelve_rate1)

        # Load another set of data for comparison and convert it to a dictionary
        df = pd.read_excel("statistic_id283093_number-of-homicides-in-england-and-wales-2002-2022.xlsx", "Data", header = 1)
        df.head()

        z = dataframe_to_dictionary(df)
        homicide_rate1 = z["Number of homicides in England and Wales 2002-2022"]

        homicide_rate = np.array(homicide_rate1)

        # Calculate the Pearson correlation coefficient and assert it's greater than or equal to 0.1
        result = PmCc(gamingtwelve_rate, homicide_rate)
        self.assertGreaterEqual(abs(result), 0.1)

# Entry point for running the tests when the script is executed
if __name__ == '__main__':
    unittest.main()