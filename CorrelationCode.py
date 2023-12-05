#import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import unittest
import Testing
from variables import video_gamer, violent_crimes
from functions import PmCc,linear_regression

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
