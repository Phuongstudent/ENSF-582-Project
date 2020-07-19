from tkintertable import TableCanvas, TableModel
from tkinter import *
import random
from collections import OrderedDict

data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
        'rec2': {'col1': 99.88, 'col2': 321.79, 'label': 'rec3'},
        'rec3': {'col1': 29.88, 'col2': 408.79, 'label': 'rec2'}
        }

from tkintertable.Testing import sampledata
#data=sampledata()
#print(data)

class TestApp(Frame):
    """Basic test frame for the table"""

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        #self.main.geometry('800x500+200+100')
        self.main.title('Test')
        f = Frame(self.main)
        f.grid(row=0, column=1, sticky="nsew")
        #f.pack(fill=tk.Y,expand=-1,side = tk.LEFT)
        table = TableCanvas(f, cellwidth=60, cellbackgr='white',
			thefont=('Arial',12),rowheight=25, rowheaderwidth=30,
			rowselectedcolor='yellow', editable=True)
        table.importCSV('2017_Traffic_Volume_Flow.csv')
        print (table.model.columnNames)
        #table.model.data[1]['a'] = 'XX'
        #table.model.setValueAt('YY',0,2)
        table.show()
        return

import tkinter as tk

window = tk.Tk()
window.title("Don and Sarim beast project")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
frame_a = tk.Frame()
frame_b = tk.Frame(master = frame_a)
frame_c = tk.Frame(master = frame_a)

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}


button_Type_Label = tk.Label(master = frame_b,text="Type", width = 25, height = 5)
button_Type_Label.pack(side = tk.LEFT)

button_Type = ttk.Combobox(master = frame_b ,text = "Type", width = 25, height = 5)
button_Type['values'] = ('Accident', 'Traffic Volume')
button_Type.pack(side = tk.LEFT)

frame_b.grid(row=0, column=0, sticky="ew", padx=10)


button_Year_Label = tk.Label(master = frame_c,text="Year", width = 25, height = 5)
button_Year_Label.pack(side = tk.LEFT)

button_Year = ttk.Combobox(master = frame_c,text = "Year", width = 25, height = 5)
button_Year['values'] = ('2016', '2017', '2018')
button_Year.pack(side = tk.LEFT)

frame_c.grid(row=1, column=0, sticky="ew", padx=10)

button_Read = tk.Button(master = frame_a,text = "Read", width = 25, height = 5)
button_Read.grid(row=2, column=0, sticky="ew", padx=10)

button_Sort = tk.Button(master = frame_a,text = "Sort", width = 25, height = 5)
button_Sort.grid(row=3, column=0, sticky="ew", padx=10)

button_Analysis = tk.Button(master = frame_a,text = "Analysis", width = 25, height = 5)
button_Analysis.grid(row=4, column=0, sticky="ew", padx=10)

button_Map = tk.Button(master = frame_a,text = "Map", width = 25, height = 5)
button_Analysis.grid(row=5, column=0, sticky="ew", padx=10)

status = tk.Label(master = frame_a,text="Status:")
status.grid(row=6, column=0, sticky="ew", padx=10)

status_display = tk.Label(master = frame_a,text="Success!", foreground = "red", background = "white")
status_display.grid(row=7, column=0, sticky="ew", padx=10)


frame_a.grid(row=0, column=0, sticky="ns")


app=TestApp()
app.grid(row=0, column=1, sticky="nsew")

window.mainloop()