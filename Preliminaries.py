# Preliminary analysis for the project proposal
import pandas as pd
import matplotlib.pyplot as plt
# Read in the data (which can be downloaded from):
# https://data.oecd.org/pisa/reading-performance-pisa.htm
# https://data.oecd.org/emp/employment-rate.htm
# https://data.oecd.org/emp/employment-by-activity.htm
# https://data.oecd.org/emp/employment-by-education-level.htm

Reading = pd.read_csv("../ReadingPerformancePisa.csv")
EmploymentRate = pd.read_csv("../EmploymentRate.csv")
SelfEmploymentRate = pd.read_csv("../SelfEmploymentRate.csv")
EmploymentActivity = pd.read_csv("../EmploymentRateByActivity.csv")
EmploymentEducation = pd.read_csv("../EmploymentRateByEducationLevel.csv")

# Concatenate all this information:
DATA = pd.concat([Reading, EmploymentRate, EmploymentActivity, EmploymentEducation])

# Focus on a single year, say 2018:
Reading = Reading[Reading["TIME"] == 2018]
EmploymentRate = EmploymentRate[EmploymentRate["TIME"] == "2018"]
SelfEmploymentRate = SelfEmploymentRate[SelfEmploymentRate["TIME"] == 2018]
EmploymentActivity = EmploymentActivity[EmploymentActivity["TIME"] == "2018"]
EmploymentEducation = EmploymentEducation[EmploymentEducation["TIME"] == 2018]

# Just look at the total employment rates regardless of gender:
# And look at the percentage fo the work force instead of the whole population
EmploymentRate = EmploymentRate[(EmploymentRate["SUBJECT"] == "TOT") & (EmploymentRate["MEASURE"] == "PC_WKGPOP")]
SelfEmploymentRate = SelfEmploymentRate[SelfEmploymentRate["SUBJECT"] == "TOT"]

employment_rate = []
reading_performance = []
for country in EmploymentRate["LOCATION"].unique():
    if country in Reading["LOCATION"].unique():
        employment_rate.append(EmploymentRate[EmploymentRate["LOCATION"] == country]["Value"].values)
        reading_performance.append(Reading[Reading["LOCATION"] == country]["Value"].values)
plt.plot(reading_performance, employment_rate, 'o', color = 'k')
plt.title('Employment rate vs. Reading performace across multiple countries')
plt.xlabel('PISA reading performace')
plt.ylabel('Employment rate (\% working pop.)')
plt.show()

self_employment_rate = []
reading_performance = []
for country in SelfEmploymentRate["LOCATION"].unique():
    if country in Reading["LOCATION"].unique():
        self_employment_rate.append(SelfEmploymentRate[SelfEmploymentRate["LOCATION"] == country]["Value"].values)
        reading_performance.append(Reading[Reading["LOCATION"] == country]["Value"].values)
plt.plot(reading_performance, self_employment_rate, 'o', color = 'k')
plt.title('Self employment rate vs. Reading performace across multiple countries')
plt.xlabel('PISA reading performace')
plt.ylabel('Self employment rate (\% of employment)')
plt.show()

print(Reading.head())
print(EmploymentRate.head())
print(SelfEmploymentRate.head())
# print(EmploymentActivity.head())
# print(EmploymentEducation.head())

