import pymongo
import dns
import matplotlib.pyplot as plt
import numpy as np
import folium
import matplotlib
matplotlib.use("TkAgg")
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from pymongo import MongoClient


class TrafficVolume:
    # create variables to store longitude and latitude of areas with greatest volume per year
    lng_2016 = None
    lat_2016 = None

    lng_2017 = None
    lat_2017 = None

    lng_2018 = None
    lat_2018 = None

    # Create empty dictionaries to be populated with data depending on year
    volume_2016 = dict()
    volume_2017 = dict()
    volume_2018 = dict()

    # Buffer that holds second dict in the dict of a dict to create table
    volume_2016_buffer = dict()
    volume_2017_buffer = dict()
    volume_2018_buffer = dict()

    # Dictionary that will sum the traffic volume for similar locations
    volume_2016_sum = dict()
    volume_2017_sum = dict()
    volume_2018_sum = dict()

    def __init__(self):

        self.cluster = MongoClient("mongodb+srv://sarim:1234@cluster0.azpgb.mongodb.net/ENSF592?retryWrites=true&w"
                                   "=majority")
        self.db = self.cluster["ENSF592"]
        self.traffic_volume_2016 = self.db["TrafficFlow2016_OpenData"]
        self.traffic_volume_2017 = self.db["2017_Traffic_Volume_Flow"]
        self.traffic_volume_2018 = self.db["Traffic_Volumes_for_2018"]

    def create_volume_sum_dict(self):
        for element in self.traffic_volume_2016.find():
            self.volume_2016_sum[element['secname']] = self.volume_2016_sum.get(element['secname'], 0) + \
                                                       element['volume']

        for element in self.traffic_volume_2017.find():
            self.volume_2017_sum[element['segment_name']] = self.volume_2017_sum.get(element['segment_name'], 0) + \
                                                            element['volume']

        for element in self.traffic_volume_2018.find():
            self.volume_2018_sum[element['SECNAME']] = self.volume_2018_sum.get(element['SECNAME'], 0) + \
                                                       element['VOLUME']

    def create_volume_table_dict(self):
        # this variable is only use to enumerate the dictionary
        i = 0
        # iterate through data collection and add incident information to corresponding dict based on 2016
        for element in self.traffic_volume_2016.find():
            # this variable is only use to skip the fist iteration
            count = 0

            for key, value in element.items():
                if count != 0:
                    if key == 'secname':
                        # Assign the total count for each incident
                        self.volume_2016_buffer["Sum of Volume"] = self.volume_2016_sum[value]
                        self.volume_2016_buffer[key] = str(value)
                    # if it is the "ID" column, use this column as the key for "incidents_2016"
                    else:
                        # assigning the column header with the row information
                        self.volume_2016_buffer[key] = str(value)

                count = count + 1
            # Store the dict into the dict of dict table
            self.volume_2016[i] = self.volume_2016_buffer.copy()
            i = i + 1

        # this variable is only use to enumerate the dictionary
        i = 0
        # iterate through data collection and add incident information to corresponding dict based on 2017
        for element in self.traffic_volume_2017.find():
            # this variable is only use to skip the fist iteration
            count = 0

            for key, value in element.items():
                if count != 0:
                    if key == 'segment_name':
                        # Assign the total count for each incident
                        self.volume_2017_buffer["Sum of Volume"] = self.volume_2017_sum[value]
                        self.volume_2017_buffer[key] = str(value)
                    # if it is the "ID" column, use this column as the key for "incidents_2016"
                    else:
                        # assigning the column header with the row information
                        self.volume_2017_buffer[key] = str(value)

                count = count + 1
            # Store the dict into the dict of dict table
            self.volume_2017[i] = self.volume_2017_buffer.copy()
            i = i + 1

        # this variable is only use to enumerate the dictionary
        i = 0
        # iterate through data collection and add incident information to corresponding dict based on 2018
        for element in self.traffic_volume_2018.find():
            # this variable is only use to skip the fist iteration
            count = 0

            for key, value in element.items():
                if count != 0:
                    if key == 'SECNAME':
                        # Assign the total count for each incident
                        self.volume_2018_buffer["Sum of Volume"] = self.volume_2018_sum[value]
                        self.volume_2018_buffer[key] = str(value)
                    # if it is the "ID" column, use this column as the key for "incidents_2016"
                    else:
                        # assigning the column header with the row information
                        self.volume_2018_buffer[key] = str(value)

                count = count + 1
            # Store the dict into the dict of dict table
            self.volume_2018[i] = self.volume_2018_buffer.copy()
            i = i + 1

    def create_volume_graph(self,parent):
        # Test creation of line graph
        f = Figure(figsize = (5,5), dpi =100)

        plt = f.add_subplot(111)
        plt.plot([2016, 2017, 2018], [max(self.volume_2016_sum.values()), max(self.volume_2017_sum.values()),
                                      max(self.volume_2018_sum.values())])
        plt.set_xticks(np.arange(2016, 2019, 1))
        plt.set_ylabel('Volume')
        plt.set_xlabel('Year')
        plt.set_title('Maximum Traffic Volume Trend Over 2016-2018')
        canvas = FigureCanvasTkAgg(f, parent)
        canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")

    def get_coord_2016(self):
        max_seg = max(self.volume_2016_sum, key=self.volume_2016_sum.get)

        for element in self.traffic_volume_2016.find():
            if element['secname'] == max_seg:
                temp = element['the_geom']

        lst = temp.split(', ')
        t = lst[1]
        lst2 = t.split()

        self.lng_2016 = float(lst2[0])
        self.lat_2016 = float(lst2[1])

    def get_coord_2017(self):
        max_seg = max(self.volume_2017_sum, key=self.volume_2017_sum.get)

        for element in self.traffic_volume_2017.find():
            if element['segment_name'] == max_seg:
                temp = element['the_geom']

        lst = temp.split(', ')
        t = lst[1]
        lst2 = t.split()

        self.lng_2017 = float(lst2[0])
        self.lat_2017 = float(lst2[1])

    def get_coord_2018(self):
        max_seg = max(self.volume_2018_sum, key=self.volume_2018_sum.get)

        for element in self.traffic_volume_2018.find():
            if element['SECNAME'] == max_seg:
                temp = element['multilinestring']

        lst = temp.split(', ')
        t = lst[1]
        lst2 = t.split()

        self.lng_2018 = float(lst2[0])
        self.lat_2018 = float(lst2[1])

    def gen_vol_map(self, latitude=0.0, longitude=0.0, year = ""):
        my_map = folium.Map(location=[latitude, longitude], zoom_start=15)

        folium.Marker([latitude, longitude], popup='Maximum Traffic Volume').add_to(my_map)

        my_map.save('Volume_Map' + year + '.html')


# Code to test some output
# vol = TrafficVolume()
# vol.create_volume_sum_dict()
# vol.create_volume_graph()
# vol.get_coord_2017()
# vol.gen_vol_map(vol.lat_2017,vol.lng_2017)
