import pymongo
import dns
import matplotlib.pyplot as plt
import numpy as np

from pymongo import MongoClient

# connect to MongoDB
cluster = MongoClient("mongodb+srv://sarim:1234@cluster0.azpgb.mongodb.net/ENSF592?retryWrites=true&w=majority")

# create variable to access database
db = cluster["ENSF592"]

# create variables to access database collections
traffic_volume_2016 = db["TrafficFlow2016_OpenData"]
traffic_volume_2017 = db["2017_Traffic_Volume_Flow"]
traffic_volume_2018 = db["Traffic_Volumes_for_2018"]

# create variables to store total traffic volume for each year
total_volume_2016 = 0
total_volume_2017 = 0
total_volume_2018 = 0

# sort the data based on descending order of traffic volume
volume_2016_sorted = traffic_volume_2016.find().sort("volume", -1)
volume_2017_sorted = traffic_volume_2017.find().sort("volume", -1)
volume_2018_sorted = traffic_volume_2018.find().sort("VOLUME", -1)

# calculate total volume of vehicles for each year and print the total volume for that year
for result in traffic_volume_2016.find():  # Need to use .find() method to return a cursor object, allowing iteration
    total_volume_2016 += result["volume"]
print("The total volume of vehicles in 2016 was", total_volume_2016)

for result in traffic_volume_2017.find():
    total_volume_2017 += result["volume"]
print("The total volume of vehicles in 2017 was", total_volume_2017)

for result in traffic_volume_2018.find():
    total_volume_2018 += result["VOLUME"]
print("The total volume of vehicles in 2018 was", total_volume_2018)


# prints the volume and location in the most congested areas for a given year
for result in volume_2016_sorted[:1]:
    print("The most congested area in 2016 was", result["secname"], "with", result["volume"], "vehicles.")

for result in volume_2017_sorted[:1]:
    print("The most congested area in 2017 was", result["segment_name"], "with", result["volume"], "vehicles.")

for result in volume_2018_sorted[:1]:
    print("The most congested area in 2018 was", result["SECNAME"], "with", result["VOLUME"], "vehicles.")

# Test creation of line graph
plt.plot([2016, 2017, 2018], [total_volume_2016, total_volume_2017, total_volume_2018])
plt.xticks(np.arange(2016, 2019, 1))
plt.ylabel('Volume')
plt.xlabel('Year')
plt.title('Maximum Traffic Volume Trend Over 2016-2018')
plt.show()
