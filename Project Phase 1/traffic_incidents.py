import pymongo
import dns
import matplotlib.pyplot as plt
import numpy as np

from pymongo import MongoClient

# Connect to MongoDB
cluster = MongoClient("mongodb+srv://sarim:1234@cluster0.azpgb.mongodb.net/ENSF592?retryWrites=true&w=majority")

# Create variable to access database
db = cluster["ENSF592"]

# Create variable to access database collections and use .find() to return as a cursor object
traffic_incidents = db["Traffic_Incidents"].find()

# create empty dictionaries to be populated with data based on year
incidents_2016 = dict()
incidents_2017 = dict()
incidents_2018 = dict()

# create variables to store the total number of incidents for each year
total_incidents_2016 = 0
total_incidents_2017 = 0
total_incidents_2018 = 0

# iterate through data collection and add incident information to corresponding dict based on year
for element in traffic_incidents:
    if element["id"][:4] == "2016":  # 2016 data
        incidents_2016[element["INCIDENT INFO"]] = incidents_2016.get(element["INCIDENT INFO"], 0) + 1
    elif element["id"][:4] == "2017":  # 2017 data
        incidents_2017[element["INCIDENT INFO"]] = incidents_2017.get(element["INCIDENT INFO"], 0) + 1
    elif element["id"][:4] == "2018":  # 2018 data
        incidents_2018[element["INCIDENT INFO"]] = incidents_2018.get(element["INCIDENT INFO"], 0) + 1
    else:
        continue

# Calculate the total number of incidents each year and print to console
total_incidents_2016 = sum(incidents_2016.values())
print("Total number of traffic incidents in 2016:", total_incidents_2016)

total_incidents_2017 = sum(incidents_2017.values())
print("Total number of traffic incidents in 2017:", total_incidents_2017)

total_incidents_2018 = sum(incidents_2018.values())
print("Total number of traffic incidents in 2018:", total_incidents_2018)

# Output the location of the maximum number of incidents and the total number of incidents for a given year
max_incidents_2016_location = max(incidents_2016, key=incidents_2016.get)
max_incidents_2016_amount = max(incidents_2016.values())
print("There were", max_incidents_2016_amount, "incidents at", max_incidents_2016_location, "in 2016")

max_incidents_2017_location = max(incidents_2017, key=incidents_2017.get)
max_incidents_2017_amount = max(incidents_2017.values())
print("There were", max_incidents_2017_amount, "incidents at", max_incidents_2017_location, "in 2017")

max_incidents_2018_location = max(incidents_2018, key=incidents_2018.get)
max_incidents_2018_amount = max(incidents_2018.values())
print("There were", max_incidents_2018_amount, "incidents at", max_incidents_2018_location, "in 2018")


# Test creation of line graph
plt.plot([2016, 2017, 2018], [total_incidents_2016, total_incidents_2017, total_incidents_2018])
plt.xticks(np.arange(2016, 2019, 1))
plt.ylabel('Volume')
plt.xlabel('Year')
plt.title('Total Incidents Trend Over 2016-2018')
plt.show()
