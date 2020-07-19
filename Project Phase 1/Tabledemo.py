from tkintertable import TableCanvas, TableModel
from tkinter import *
import random
from collections import OrderedDict


# Example of how to create and import data as dictionary
# data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
#        'rec2': {'col1': 99.88, 'col2': 321.79, 'label': 'rec3'},
#        'rec3': {'col1': 29.88, 'col2': 408.79, 'label': 'rec2'}
#        }


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
        table = TableCanvas(f, cellwidth=60, cellbackgr='white', thefont=('Arial',12),rowheight=25, rowheaderwidth=30, rowselectedcolor='yellow', editable=True)

        #Import table from csv
        table.importCSV('2017_Traffic_Volume_Flow.csv')

        """if importing table as dictionary, use this: data is of type dictionary
        """
        # table = TableCanvas(f, cellwidth=60, data = data, cellbackgr='white',
        #                    thefont=('Arial', 12), rowheight=25, rowheaderwidth=30,
        #                    rowselectedcolor='yellow', editable=True)

        print (table.model.columnNames)
        table.show()
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