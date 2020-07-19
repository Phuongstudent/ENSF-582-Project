from tkintertable import TableCanvas, TableModel
from tkinter import *
import random
from collections import OrderedDict
import pymongo
import dns
import matplotlib.pyplot as plt
import numpy as np

from pymongo import MongoClient

# Example of how to create and import data as dictionary
# data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
#        'rec2': {'col1': 99.88, 'col2': 321.79, 'label': 'rec3'},
#        'rec3': {'col1': 29.88, 'col2': 408.79, 'label': 'rec2'}
#        }



# Connect to MongoDB
cluster = MongoClient("mongodb+srv://sarim:1234@cluster0.azpgb.mongodb.net/ENSF592?retryWrites=true&w=majority")

# Create variable to access database
db = cluster["ENSF592"]

# Create variable to access database collections and use .find() to return as a cursor object
traffic_incidents = db["Traffic_Incidents"].find()



# create empty dictionaries to be populated with data based on year
incidents_2016 = dict()
# buffer that hold the second dict in the dict of dict for the table
incidents_2016_buffer = dict()

incidents_2017 = dict()
# buffer that hold the second dict in the dict of dict for the table
incidents_2017_buffer = dict()

incidents_2018 = dict()
# buffer that hold the second dict in the dict of dict for the table
incidents_2018_buffer = dict()

# dict that hold the total count of each incident info
incident_2016_sum = dict()
incident_2017_sum = dict()
incident_2018_sum = dict()
# Hold a copy of "Traffic_Incidents" , to be used to get the total count of each incident info
traffic_incidents_Copy = db["Traffic_Incidents"].find()

# Loop to get the total count of each incident info
for element in traffic_incidents_Copy:
    if element["id"][:4] == "2016":  # 2016 data
            incident_2016_sum[element["INCIDENT INFO"]] = incident_2016_sum.get(element["INCIDENT INFO"], 0) + 1
    elif element["id"][:4] == "2017":  # 2017 data
            incident_2017_sum[element["INCIDENT INFO"]] = incident_2017_sum.get(element["INCIDENT INFO"], 0) + 1
    elif element["id"][:4] == "2018":  # 2018 data
            incident_2018_sum[element["INCIDENT INFO"]] = incident_2018_sum.get(element["INCIDENT INFO"], 0) + 1
    else:
        continue

# iterate through data collection and add incident information to corresponding dict based on year
for element in traffic_incidents:
    # this variable is only use to skip the fist iteration
    count = 0
    for key,value in element.items():
        #skip the first iteration, since the first iteration is just "_id" in the collection
        if count != 0:
            if element["id"][:4] == "2016":  # 2016 data
                if key == 'INCIDENT INFO':
                    #Assign the total count for each incident
                    incidents_2016_buffer["Sum of Incidents"] = incident_2016_sum[value]
                    incidents_2016_buffer[key] = str(value)
                elif key != 'id':
                    # assigning the column header with the row information
                    incidents_2016_buffer[key] = str(value)
                # if it is the "ID" column, use this column as the key for "incidents_2016"
                else:
                    # assigning the column header with the row information
                    incidents_2016_buffer[key] = str(value)
                    # Store the dict into the dict of dict table
                    incidents_2016[value] = incidents_2016_buffer.copy()

            if element["id"][:4] == "2017":  # 2017 data
                if key == 'INCIDENT INFO':
                    # Assign the total count for each incident
                    incidents_2017_buffer["Sum of Incidents"] = incident_2017_sum[value]
                    incidents_2017_buffer[key] = str(value)
                elif key != "id":
                    # assigning the column header with the row information
                    incidents_2017_buffer[key] = str(value)
                # if it is the "ID" column, use this column as the key for "incidents_2016"
                else:
                    # assigning the column header with the row information
                    incidents_2017_buffer[key] = str(value)
                    # Store the dict into the dict of dict table
                    incidents_2017[value] = incidents_2017_buffer.copy()
            if element["id"][:4] == "2018":  # 2018 data
                if key == 'INCIDENT INFO':
                    # Assign the total count for each incident
                    incidents_2018_buffer["Sum of Incidents"] = incident_2018_sum[value]
                    incidents_2018_buffer[key] = str(value)
                elif key != "id":
                    # assigning the column header with the row information
                    incidents_2018_buffer[key] = str(value)
                # if it is the "ID" column, use this column as the key for "incidents_2016"
                else:
                    # assigning the column header with the row information
                    incidents_2018_buffer[key] = str(value)
                    # Store the dict into the dict of dict table
                    incidents_2018[value] = incidents_2018_buffer.copy()

        # this variable is only use to skip the fist iteration
        count = count + 1




# Class in charge of creating, displaying and manipulating table
class TestApp(Frame):
    """Basic test frame for the table"""

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.title('Test')
        # Initialize frame for the table
        f = Frame(self.main)

        # Initialize the grid location of the table
        f.grid(row=0, column=1, sticky="nsew")

        # no need to pack since we using grid geometry
        # f.pack(fill=tk.Y,expand=-1,side = tk.LEFT)

        # Create/Format table
        table = TableCanvas(f, cellwidth=60, data = incidents_2016, cellbackgr='white', thefont=('Arial',12),rowheight=25, rowheaderwidth=30, rowselectedcolor='yellow', editable=True)

        #Import table from csv
        #table.importCSV('2017_Traffic_Volume_Flow.csv')

        """if importing table as dictionary, use this: data is of type dictionary
        """
        # table = TableCanvas(f, cellwidth=60, data = data, cellbackgr='white',
        #                    thefont=('Arial', 12), rowheight=25, rowheaderwidth=30,
        #                    rowselectedcolor='yellow', editable=True)

        print (table.model.columnNames)
        table.show()
        # sort the first column from highest to lowest (the sum of incident column)
        table.sortTable(reverse=1)

        return

import tkinter as tk

# set up canvas and title
window = tk.Tk()
window.title("Don and Sarim beast project")

# Configure window size and expansion ratio
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Left frame that hold all buttons
frame_a = tk.Frame()

# Frame within frame_a to hold 1 label and 1 combobox
frame_b = tk.Frame(master = frame_a)

# Frame within frame_a to hold 1 label and 1 combobox
frame_c = tk.Frame(master = frame_a)

# Label for "Type" button
button_Type_Label = tk.Label(master = frame_b,text="Type", width = 25, height = 5)
# Position from left to right
button_Type_Label.pack(side = tk.LEFT)
# Combobox for "Type" button
button_Type = ttk.Combobox(master = frame_b ,text = "Type", width = 25, height = 5)
button_Type['values'] = ('Accident', 'Traffic Volume')
# Position from left to right
button_Type.pack(side = tk.LEFT)
# Group combobox and label into one frame, and position within frame_a, first row, extend horizontally
frame_b.grid(row=0, column=0, sticky="ew", padx=10)

# Label for "Year" button
button_Year_Label = tk.Label(master = frame_c,text="Year", width = 25, height = 5)
button_Year_Label.pack(side = tk.LEFT)
# Combobox for "Year" button
button_Year = ttk.Combobox(master = frame_c,text = "Year", width = 25, height = 5)
button_Year['values'] = ('2016', '2017', '2018')
# Position from left to right
button_Year.pack(side = tk.LEFT)
# Group combobox and label into one frame, and position within frame_a, second row, extend horizontally
frame_c.grid(row=1, column=0, sticky="ew", padx=10)

# "Read" button
button_Read = tk.Button(master = frame_a,text = "Read", width = 25, height = 5)
# position as third row within grid, extend horizontally
button_Read.grid(row=2, column=0, sticky="ew", padx=10)

# "Sort" button
button_Sort = tk.Button(master = frame_a,text = "Sort", width = 25, height = 5)
# position as fourth row within grid, extend horizontally
button_Sort.grid(row=3, column=0, sticky="ew", padx=10)

# "Analysis" button
button_Analysis = tk.Button(master = frame_a,text = "Analysis", width = 25, height = 5)
# position as fifth row within grid, extend horizontally
button_Analysis.grid(row=4, column=0, sticky="ew", padx=10)

# "Map" button
button_Map = tk.Button(master = frame_a,text = "Map", width = 25, height = 5)
# position as sixth row within grid, extend horizontally
button_Analysis.grid(row=5, column=0, sticky="ew", padx=10)

# "Status" label
status = tk.Label(master = frame_a,text="Status:")
# position as seventh row within grid, extend horizontally
status.grid(row=6, column=0, sticky="ew", padx=10)

# "Status" display
status_display = tk.Label(master = frame_a,text="Success!", foreground = "red", background = "white")
# position as eighth row within grid, extend horizontally
status_display.grid(row=7, column=0, sticky="ew", padx=10)

# Situate frame_a to the left, first row and column extend vertically
frame_a.grid(row=0, column=0, sticky="ns")

# initialize table
app=TestApp()
# add table to first row, second column, extend everywhere
app.grid(row=0, column=1, sticky="nsew")

# Keep listening for events
window.mainloop()

















