#import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import unittest
import Testing
from functions import PmCc,linear_regression

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

x = video_gamer
y = violent_crimes

test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(Testing.TestFunction1))

# Plotting
plt.figure()
plt.plot(video_gamer, violent_crimes, 'o')

if test_result.wasSuccessful():
    # Linear regression if the test is successful
    lin_reg_m_main, lin_reg_q_main = linear_regression(video_gamer, violent_crimes)
    y_main = lin_reg_m_main * video_gamer + lin_reg_q_main
    plt.plot(video_gamer, y_main, label="Regression line")
    # Calculate and display PMCC
    plt.text(0.75, 1.035, f"PMCC: {PmCc(video_gamer, violent_crimes):.2f} > Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')
else:
    # Display a message if the test is not successful
    plt.text(0.75, 1.035, f"PMCC: {PmCc(video_gamer, violent_crimes):.2f} > No Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')

plt.xlabel("Video gaming rate (%)")
plt.ylabel("Weapon possessions")
plt.title("Adult video gaming and weapon possessions correlation")

plt.legend()

# Display the plot
plt.show()
