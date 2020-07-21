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


class TrafficIncidents:
    # create variables to store longitude and latitude of areas with greatest volume per year
    lng_2016 = None
    lat_2016 = None

    lng_2017 = None
    lat_2017 = None

    lng_2018 = None
    lat_2018 = None

    # Create empty dictionaries to be populated with data depending on year
    incidents_2016 = dict()
    incidents_2017 = dict()
    incidents_2018 = dict()

    # Buffer that holds second dict in the dict of a dict to create table
    incidents_2016_buffer = dict()
    incidents_2017_buffer = dict()
    incidents_2018_buffer = dict()

    # Dictionary that will hold the sum of traffic incidents for the same location per year
    incident_2016_sum = dict()
    incident_2017_sum = dict()
    incident_2018_sum = dict()

    def __init__(self):

        self.cluster = MongoClient("mongodb+srv://sarim:1234@cluster0.azpgb.mongodb.net/ENSF592?retryWrites=true&w"
                                   "=majority")
        self.db = self.cluster["ENSF592"]
        self.traffic_incidents = self.db["Traffic_Incidents"]

    def create_incident_sum_dict(self):

        for element in self.traffic_incidents.find():
            if element["id"][:4] == "2016":  # 2016 data
                self.incident_2016_sum[element["INCIDENT INFO"]] = \
                    self.incident_2016_sum.get(element["INCIDENT INFO"], 0) + 1

            elif element["id"][:4] == "2017":  # 2017 data
                self.incident_2017_sum[element["INCIDENT INFO"]] = \
                    self.incident_2017_sum.get(element["INCIDENT INFO"], 0) + 1

            elif element["id"][:4] == "2018":  # 2018 data
                self.incident_2018_sum[element["INCIDENT INFO"]] = \
                    self.incident_2018_sum.get(element["INCIDENT INFO"], 0) + 1

            else:
                continue

    def create_incident_table_dict(self):
        # iterate through data collection and add incident information to corresponding dict based on year
        for element in self.traffic_incidents.find():
            # this variable is only use to skip the fist iteration
            count = 0
            for key, value in element.items():
                # skip the first iteration, since the first iteration is just "_id" in the collection
                if count != 0:
                    if element["id"][:4] == "2016":  # 2016 data
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

    def create_incidents_graph(self, parent):
        # Test creation of line graph
        f = Figure(figsize=(5, 5), dpi=100)
        plt = f.add_subplot(111)
        plt.plot([2016, 2017, 2018], [max(self.incident_2016_sum.values()), max(self.incident_2017_sum.values()),
                                      max(self.incident_2018_sum.values())])
        plt.set_xticks(np.arange(2016, 2019, 1))
        plt.set_ylabel('Volume')
        plt.set_xlabel('Year')
        plt.set_title('Maximum Traffic Incidents Trend Over 2016-2018')
        canvas = FigureCanvasTkAgg(f, parent)
        canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")

    def get_coord_2016(self):
        max_seg = max(self.incident_2016_sum, key=self.incident_2016_sum.get)

        for element in self.traffic_incidents.find():
            if element['id'][:4] == '2016' and element['INCIDENT INFO'] == max_seg:
                self.lng_2016 = element['Longitude']
                self.lat_2016 = element['Latitude']

    def get_coord_2017(self):
        max_seg = max(self.incident_2017_sum, key=self.incident_2017_sum.get)

        for element in self.traffic_incidents.find():
            if element['id'][:4] == '2017' and element['INCIDENT INFO'] == max_seg:
                self.lng_2017 = element['Longitude']
                self.lat_2017 = element['Latitude']

    def get_coord_2018(self):
        max_seg = max(self.incident_2018_sum, key=self.incident_2018_sum.get)

        for element in self.traffic_incidents.find():
            if element['id'][:4] == '2018' and element['INCIDENT INFO'] == max_seg:
                self.lng_2018 = element['Longitude']
                self.lat_2018 = element['Latitude']

    def gen_incident_map(self, latitude=0.0, longitude=0.0, year=""):
        my_map = folium.Map(location=[latitude, longitude], zoom_start=15)

        folium.Marker([latitude, longitude], popup='Maximum Traffic Incidents').add_to(my_map)

        my_map.save('Incident_Map' + year + '.html')


# Code to test some methods
# t = TrafficIncidents()
# t.create_incident_sum_dict()
# t.create_incidents_graph()
# t.get_coord_2017()
# t.gen_incident_map(t_incidents.lat_2017, t_incidents.lng_2017)

