#import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import unittest
import Testing
from variables import video_gamer, gamingtwelve_rate, data_dates, violent_crimes, sexual_offences, weapon_possession,suicide_rate,homicide_rate
from functions import PmCc,linear_regression

x = video_gamer

test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(Testing.TestFunction1))

y = violent_crimes
# Plotting
plt.figure()
plt.plot(x, y, 'o')

if test_result.wasSuccessful():
    # Linear regression if the test is successful
    lin_reg_m_main, lin_reg_q_main = linear_regression(x, y)
    y_main = lin_reg_m_main * x+ lin_reg_q_main
    plt.plot(x, y_main, label="Regression line")
    # Calculate and display PMCC
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')
else:
    # Display a message if the test is not successful
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > No Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')

plt.xlabel("Video gaming rate (%)")
plt.ylabel("Number of Violent crimes")
plt.title("Adult video gaming and violent crime correlation")

plt.legend()

# Display the plot
plt.show()

test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(Testing.TestFunction1))

y = sexual_offences
# Plotting
plt.figure()
plt.plot(x, y, 'o')

if test_result.wasSuccessful():
    # Linear regression if the test is successful
    lin_reg_m_main, lin_reg_q_main = linear_regression(x, y)
    y_main = lin_reg_m_main * x+ lin_reg_q_main
    plt.plot(x, y_main, label="Regression line")
    # Calculate and display PMCC
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')
else:
    # Display a message if the test is not successful
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > No Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')

plt.xlabel("Video gaming rate (%)")
plt.ylabel("Number of Sexual offences")
plt.title("Adult video gaming and sexual offences correlation")

plt.legend()

# Display the plot
plt.show()

test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(Testing.TestFunction1))

y = weapon_possession
# Plotting
plt.figure()
plt.plot(x, y, 'o')

if test_result.wasSuccessful():
    # Linear regression if the test is successful
    lin_reg_m_main, lin_reg_q_main = linear_regression(x, y)
    y_main = lin_reg_m_main * x+ lin_reg_q_main
    plt.plot(x, y_main, label="Regression line")
    # Calculate and display PMCC
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')
else:
    # Display a message if the test is not successful
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > No Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')

plt.xlabel("Video gaming rate (%)")
plt.ylabel("Number of Weapon possession")
plt.title("Adult video gaming and weapon possession correlation")

plt.legend()

# Display the plot
plt.show()

test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(Testing.TestFunction1))

y = suicide_rate
# Plotting
plt.figure()
plt.plot(x, y, 'o')

if test_result.wasSuccessful():
    # Linear regression if the test is successful
    lin_reg_m_main, lin_reg_q_main = linear_regression(x, y)
    y_main = lin_reg_m_main * x+ lin_reg_q_main
    plt.plot(x, y_main, label="Regression line")
    # Calculate and display PMCC
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')
else:
    # Display a message if the test is not successful
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > No Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')

plt.xlabel("Video gaming rate (%)")
plt.ylabel("Suicide rate")
plt.title("Adult video gaming and suicide rate correlation")

plt.legend()

# Display the plot
plt.show()

x = gamingtwelve_rate

test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(Testing.TestFunction1))

y = homicide_rate
# Plotting
plt.figure()
plt.plot(x, y, 'o')

if test_result.wasSuccessful():
    # Linear regression if the test is successful
    lin_reg_m_main, lin_reg_q_main = linear_regression(x, y)
    y_main = lin_reg_m_main * x+ lin_reg_q_main
    plt.plot(x, y_main, label="Regression line")
    # Calculate and display PMCC
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')
else:
    # Display a message if the test is not successful
    plt.text(0.75, -0.09, f"PMCC: {PmCc(x, y):.2f} > No Successful Correlation", transform=plt.gca().transAxes, fontsize=5, verticalalignment='top')

plt.xlabel("Video gaming rate (%)")
plt.ylabel("Homicide rate")
plt.title("Adult video gaming and homicide rate correlation")

plt.legend()

# Display the plot
plt.show()