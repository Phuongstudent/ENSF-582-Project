from tkintertable import TableCanvas, TableModel
from tkinter import *
import random
from collections import OrderedDict
import pymongo
import dns
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from TableData import App
from traffic_incidents import TrafficIncidents
from pymongo import MongoClient


trafficIncident = TrafficIncidents()
trafficIncident.create_incident_sum_dict()
trafficIncident.create_incident_table_dict()


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

# Right frame initially
frame_d = tk.Frame()
# "Status" display
initial_display = tk.Label(master = frame_d, text="Please choose the 'Type' and 'Year' of the report", foreground = "red", background = "white", width = 100, height = 50)
initial_display.pack(side = tk.TOP)
frame_d.grid(row=0, column=1, sticky="nsew")






# Label for "Type" button
button_Type_Label = tk.Label(master = frame_b,text="Type", width = 25, height = 5)
# Position from left to right
button_Type_Label.pack(side = tk.LEFT)
# Combobox for "Type" button
button_Type = ttk.Combobox(master = frame_b ,text = "Type", width = 25, height = 5,  state="readonly")
button_Type['values'] = ('Accident', 'Traffic Volume')
# Position from left to right
button_Type.pack(side = tk.LEFT)
# Group combobox and label into one frame, and position within frame_a, first row, extend horizontally
frame_b.grid(row=0, column=0, sticky="ew", padx=10)

# Label for "Year" button
button_Year_Label = tk.Label(master = frame_c,text="Year", width = 25, height = 5)
button_Year_Label.pack(side = tk.LEFT)
# Combobox for "Year" button
button_Year = ttk.Combobox(master = frame_c,text = "Year", width = 25, height = 5, state="readonly")
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

# Incident 2016
table_incident2016 = App(window)

# Incident 2017
table_incident2017 = App(window)
# table_incident2017.importData(trafficIncident.incidents_2017)
# Incident 2018
table_incident2018 = App(window)
# table_incident2018.importData(trafficIncident.incidents_2018)

#Volume 2016
# table_volume2016 = App(window)
# table_volume2016.importData(trafficIncident.incidents_2016)

#flag variables
type_check_accident = False
type_check_trafficvolume = False
year_check2016 = False
year_check2017 = False
year_check2018 = False


# Callbacks function for Type button
def callback_button_type(event):
    global type_check_accident
    global type_check_trafficvolume
    type_check_accident = False
    type_check_trafficvolume = False
    if button_Type.get() == "Accident":
        type_check_accident = True
    elif button_Type.get() == "Traffic Volume":
        type_check_trafficvolume = True
# Event listener for when a combo is selected
button_Type.bind("<<ComboboxSelected>>", callback_button_type)


# Callbacks function for Year Button
def callback_button_Year(event):
    global year_check2016
    global year_check2017
    global year_check2018
    year_check2016 = False
    year_check2017 = False
    year_check2018 = False
    if button_Year.get() == "2016":
        year_check2016 = True
    elif button_Year.get() == "2017":
        year_check2017 = True
    elif button_Year.get() == "2018":
        year_check2018 = True
# Event listener for when a combo is selected
button_Year.bind("<<ComboboxSelected>>", callback_button_Year)


# Callbacks function for Read Button
def callback_button_Read(event):
    if type_check_accident==True and year_check2016==True:
        table_incident2017.grid_forget()
        table_incident2018.grid_forget()
        table_incident2016.importData(trafficIncident.incidents_2016)
    elif type_check_accident==True and year_check2017==True:
        table_incident2016.grid_forget()
        table_incident2018.grid_forget()
        table_incident2017.importData(trafficIncident.incidents_2017)
    elif type_check_accident==True and year_check2018==True:
        table_incident2017.grid_forget()
        table_incident2016.grid_forget()
        table_incident2018.importData(trafficIncident.incidents_2018)
# Event listener for when the button is clicked
button_Read.bind("<Button-1>", callback_button_Read)


# Callbacks function for Sort Button
def callback_button_Sort(event):
    table_incident2016.sortData(1)
    table_incident2017.sortData(1)
    table_incident2018.sortData(1)
# Event listener for when the button is clicked
button_Sort.bind("<Button-1>", callback_button_Sort)


# to be implemented for analysis button
def callback_button_Analysis(event):
    print("New Element Selected")
button_Analysis.bind("<Button-1>", callback_button_Analysis)

# to be implemented for map button
def callback_button_Map(event):
    print("New Element Selected")
button_Map.bind("<Button-1>", callback_button_Map)





# Keep listening for events
window.mainloop()

















