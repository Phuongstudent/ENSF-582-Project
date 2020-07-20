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

    # Create empty dictionaries to be populated with data depending on year
    volume_2016 = dict()
    volume_2017 = dict()
    volume_2018 = dict()

    # Buffer that holds second dict in the dict of a dict to create table
    volume_2016_buffer = dict()
    volume_2017_buffer = dict()
    volume_2018_buffer = dict()

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

    def create_volume_table_dict(self):
        # iterate through data collection and add incident information to corresponding dict based on year
        for element in self.traffic_volume_2016:
            # this variable is only use to skip the fist iteration
            count = 0
            for key, value in element.items():
                # skip the first iteration, since the first iteration is just "_id" in the collection
                if count != 0:
                    if key == 'INCIDENT INFO':
                        # Assign the total count for each incident
                        self.incidents_2016_buffer["Sum of Incidents"] = self.incident_2016_sum[value]
                        self.incidents_2016_buffer[key] = str(value)
                    elif key != 'id':
                        # assigning the column header with the row information
                        self.incidents_2016_buffer[key] = str(value)
                    # if it is the "ID" column, use this column as the key for "incidents_2016"
                    else:
                        # assigning the column header with the row information
                        self.incidents_2016_buffer[key] = str(value)
                        # Store the dict into the dict of dict table
                        self.incidents_2016[value] = self.incidents_2016_buffer.copy()

                    if element["id"][:4] == "2017":  # 2017 data
                        if key == 'INCIDENT INFO':
                            # Assign the total count for each incident
                            self.incidents_2017_buffer["Sum of Incidents"] = self.incident_2017_sum[value]
                            self.incidents_2017_buffer[key] = str(value)
                        elif key != "id":
                            # assigning the column header with the row information
                            self.incidents_2017_buffer[key] = str(value)
                        # if it is the "ID" column, use this column as the key for "incidents_2016"
                        else:
                            # assigning the column header with the row information
                            self.incidents_2017_buffer[key] = str(value)
                            # Store the dict into the dict of dict table
                            self.incidents_2017[value] = self.incidents_2017_buffer.copy()
                    if element["id"][:4] == "2018":  # 2018 data
                        if key == 'INCIDENT INFO':
                            # Assign the total count for each incident
                            self.incidents_2018_buffer["Sum of Incidents"] = self.incident_2018_sum[value]
                            self.incidents_2018_buffer[key] = str(value)
                        elif key != "id":
                            # assigning the column header with the row information
                            self.incidents_2018_buffer[key] = str(value)
                        # if it is the "ID" column, use this column as the key for "incidents_2016"
                        else:
                            # assigning the column header with the row information
                            self.incidents_2018_buffer[key] = str(value)
                            # Store the dict into the dict of dict table
                            self.incidents_2018[value] = self.incidents_2018_buffer.copy()

                # this variable is only use to skip the fist iteration
                count = count + 1

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