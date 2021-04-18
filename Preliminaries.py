# Preliminary analysis for the project proposal
import pandas as pd
# Read in the data (which can be downloaded from):
# https://data.oecd.org/pisa/reading-performance-pisa.htm
# https://data.oecd.org/emp/employment-rate.htm
# https://data.oecd.org/emp/employment-by-activity.htm
# https://data.oecd.org/emp/employment-by-education-level.htm

Reading = pd.read_csv("../ReadingPerformancePisa.csv")
EmploymentRate = pd.read_csv("../EmploymentRate.csv")
EmploymentActivity = pd.read_csv("../EmploymentRateByActivity.csv")
EmploymentEducation = pd.read_csv("../EmploymentRateByEducationLevel.csv")

# Concatenate all this information:
DATA = pd.concat([Reading, EmploymentRate, EmploymentActivity, EmploymentEducation])

# Focus on a single year, say 2018:
Reading = Reading[Reading["TIME"] == 2018]
EmploymentRate = EmploymentRate[EmploymentRate["TIME"] == "2018"]
EmploymentActivity = EmploymentActivity[EmploymentActivity["TIME"] == "2018"]
EmploymentEducation = EmploymentEducation[EmploymentEducation["TIME"] == 2018]

# Just look at the total employment rates regardless of gender:
# And look at the percentage fo the work force instead of the whole population
EmploymentRate = EmploymentRate[(EmploymentRate["SUBJECT"] == "TOT") & (EmploymentRate["MEASURE"] == "PC_WKGPOP")]


# Focus on the employment rate and reading performance
Data1 = DATA[((DATA["INDICATOR"] == "EMP") | (DATA["INDICATOR"] == "PISAREAD")) 
& ((DATA["TIME"] == 2018) | (DATA["TIME"] == "2018")) & (DATA["MEASURE"] == "PC_WKGPOP")]
print(Data1.head())
print(Reading.head())
print(EmploymentRate.head())
print(EmploymentActivity.head())
print(EmploymentEducation.head())

