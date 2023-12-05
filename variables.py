import numpy as np
import pandas as pd

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

df = pd.read_excel("statistic_id288256_number-of-violent-crime-offences-in-england-and-wales-2007-2022.xlsx", "Data", header = 3)
df.head()
print(df)

x = dataframe_to_dictionary(df)
violent_crimes1 = x["Crimes"]

z = dataframe_to_dictionary(df)
data_dates1 = z["Date"]

violent_crimes = np.array(violent_crimes1)
print(violent_crimes)

data_dates = np.array(data_dates1)
print(data_dates)