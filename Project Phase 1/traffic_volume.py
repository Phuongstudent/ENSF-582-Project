import pymongo
import dns
import matplotlib.pyplot as plt
import numpy as np

from pymongo import MongoClient


class TrafficVolume:

    # create variables to store total traffic volume for each year
    total_volume_2016 = 0
    total_volume_2017 = 0
    total_volume_2018 = 0

    def __init__(self):

        self.cluster = MongoClient("mongodb+srv://sarim:1234@cluster0.azpgb.mongodb.net/ENSF592?retryWrites=true&w"
                                   "=majority")
        self.db = self.cluster["ENSF592"]
        self.traffic_volume_2016 = self.db["TrafficFlow2016_OpenData"]
        self.traffic_volume_2017 = self.db["2017_Traffic_Volume_Flow"]
        self.traffic_volume_2018 = self.db["Traffic_Volumes_for_2018"]

    def calculate_total_volume(self):
        # calculate total volume of vehicles for each year and print the total volume for that year
        # Need to use .find() method to return a cursor object,allowing iteration
        for result in self.traffic_volume_2016.find():
            self.total_volume_2016 += result["volume"]

        for result in self.traffic_volume_2017.find():
            self.total_volume_2017 += result["volume"]

        for result in self.traffic_volume_2018.find():
            self.total_volume_2018 += result["VOLUME"]

    def create_volume_graph(self):
        # Test creation of line graph
        plt.plot([2016, 2017, 2018], [self.total_volume_2016, self.total_volume_2017, self.total_volume_2018])
        plt.xticks(np.arange(2016, 2019, 1))
        plt.ylabel('Volume')
        plt.xlabel('Year')
        plt.title('Maximum Traffic Volume Trend Over 2016-2018')
        plt.show()


vol = TrafficVolume()
vol.calculate_total_volume()
vol.create_volume_graph()