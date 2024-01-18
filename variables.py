import numpy as np
import pandas as pd

# Function to convert a pandas dataframe to a dictionary for easier data manipulation
def dataframe_to_dictionary(df):
    dictionary = {}
    for header in df:
        dictionary[header] = [data for data in df[header]]
    return dictionary

df = pd.read_excel("statistic_id300521_uk-gaming-reach-2007-2021.xlsx", "Data", header = 2)
df.head()
print(df)

y = dataframe_to_dictionary(df)
video_gamer1 = y["Gamers"]

z = dataframe_to_dictionary(df)
data_dates1 = z["UK gaming reach 2007-2021"]

video_gamer = np.array(video_gamer1)
print(video_gamer)

data_dates = np.array(data_dates1)
print(data_dates)

df = pd.read_excel("statistic_id283093_number-of-homicides-in-england-and-wales-2002-2022.xlsx", "Data2", header = 2)
df.head()
print(df)

z = dataframe_to_dictionary(df)
twelve_dates1 = z["Year"]

z = dataframe_to_dictionary(df)
gamingtwelve_rate1 = z["Games"]

twelve_dates = np.array(twelve_dates1)
print(twelve_dates)

gamingtwelve_rate = np.array(gamingtwelve_rate1)
print(gamingtwelve_rate)

df = pd.read_excel("statistic_id288256_number-of-violent-crime-offences-in-england-and-wales-2007-2022.xlsx", "Data", header = 3)
df.head()
print(df)

x = dataframe_to_dictionary(df)
violent_crimes1 = x["Crimes"]

violent_crimes = np.array(violent_crimes1)
print(violent_crimes)

df = pd.read_excel("Figure_10__Suspects_convicted_of_homicide_show_a_younger_age_profile (2).xlsx", "Data5", header = 2)
df.head()
print(df)

y = dataframe_to_dictionary(df)
sexual_offences1 = y["Sexual Offences"]

sexual_offences = np.array(sexual_offences1)
print(sexual_offences)

df = pd.read_excel("statistic_id828895_number-of-possession-of-weapon.xlsx", "Data", header = 2)
df.head()
print(df)

y = dataframe_to_dictionary(df)
weapon_possession1 = y["weapon possession"]

weapon_possession = np.array(weapon_possession1)
print(weapon_possession)

df = pd.read_excel("statistic_id283093_number-of-homicides-in-england-and-wales-2002-2022.xlsx", "Data", header = 1)
df.head()
print(df)

z = dataframe_to_dictionary(df)
twelve_dates1 = z["Year"]

z = dataframe_to_dictionary(df)
homicide_rate1 = z["Number of homicides in England and Wales 2002-2022"]

twelve_dates = np.array(twelve_dates1)
print(twelve_dates)

homicide_rate = np.array(homicide_rate1)
print(homicide_rate)

df = pd.read_excel("statistic_id282160_suicide-rate-in-england-and-wales-2000-2021 (1).xlsx", "Data", header = 3)
df.head()
print(df)

y = dataframe_to_dictionary(df)
suicide_rate1 = y["Suicide rate "]

suicide_rate = np.array(suicide_rate1)
print(suicide_rate)