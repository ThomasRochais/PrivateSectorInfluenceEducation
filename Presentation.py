# Preliminary analysis for the project proposal
import pandas as pd
import matplotlib.pyplot as plt
# Read in the data (which can be downloaded from):
# https://data.oecd.org/pisa/reading-performance-pisa.htm
# https://data.oecd.org/eduresource/public-spending-on-education.htm
# The Program for International Student Assessment (PISA) is 
# an internationally standardised assessment that was jointly developed 
# by participating countries and administered to 15-year-olds in schools.
Reading = pd.read_csv("../ReadingPerformancePISA.csv")
Math = pd.read_csv("../MathPerformancePISA.csv")
Science = pd.read_csv("../SciencePerformancePISA.csv")
PublicSpending = pd.read_csv("../PublicSpendingEducation.csv")

# print(PublicSpending.SUBJECT.unique()) # ['TRY' 'PRY_NTRY' 'PRY_TRY']

Reading = Reading[(Reading["SUBJECT"] == "TOT") & (Reading["TIME"] == 2015)]
Math = Math[(Math["SUBJECT"] == "TOT") & (Math["TIME"] == 2015)]
Science = Science[(Science["SUBJECT"] == "TOT") & (Science["TIME"] == 2015)]
PublicSpending = PublicSpending[(PublicSpending["SUBJECT"] == "PRY_NTRY") & (PublicSpending["TIME"] == 2015)]


public_spending = []
reading_performance = []
countries = []
for country in PublicSpending["LOCATION"].unique():
    if country in Reading["LOCATION"].unique():
        countries.append(country)
        public_spending.append(PublicSpending[PublicSpending["LOCATION"] == country]["Value"].values)
        reading_performance.append(Reading[Reading["LOCATION"] == country]["Value"].values)
# print(len(countries))
plt.plot(public_spending, reading_performance, 'o', color = 'k')
plt.title('PISA reading performance vs. Public spending across multiple countries')
plt.xlabel('Public spending on education (% of GDP)')
plt.ylabel('PISA reading performace')
plt.show()

public_spending = []
math_performance = []
countries = []
for country in PublicSpending["LOCATION"].unique():
    if country in Math["LOCATION"].unique():
        countries.append(country)
        public_spending.append(PublicSpending[PublicSpending["LOCATION"] == country]["Value"].values)
        math_performance.append(Math[Math["LOCATION"] == country]["Value"].values)
# print(len(countries))
plt.plot(public_spending, math_performance, 'o', color = 'k')
plt.title('PISA math performance vs. Public spending across multiple countries')
plt.xlabel('Public spending on education (% of GDP)')
plt.ylabel('PISA math performace')
plt.show()

public_spending = []
science_performance = []
countries = []
for country in PublicSpending["LOCATION"].unique():
    if country in Science["LOCATION"].unique():
        countries.append(country)
        public_spending.append(PublicSpending[PublicSpending["LOCATION"] == country]["Value"].values)
        science_performance.append(Science[Science["LOCATION"] == country]["Value"].values)
# print(len(countries))
plt.plot(public_spending, science_performance, 'o', color = 'k')
plt.title('PISA science performance vs. Public spending across multiple countries')
plt.xlabel('Public spending on education (% of GDP)')
plt.ylabel('PISA science performace')
plt.show()

# print(Reading.head())
# print(PublicSpending.head())

# print(Reading.LOCATION.unique())
# print(Math.LOCATION.unique())
# print(Science.LOCATION.unique())
# print(PublicSpending.LOCATION.unique())