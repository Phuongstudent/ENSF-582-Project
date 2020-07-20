from tkintertable import TableCanvas, TableModel
from tkinter import *
import tkinter as tk

# Class in charge of creating, displaying and manipulating table
class App(Frame):
    """Basic test frame for the table"""
    data = {}
    table = TableCanvas
    def __init__(self, parent=None):

        self.table = TableCanvas
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.title('Test')
        # Initialize frame for the table
        #f = Frame(self.main)

        # Initialize the grid location of the table
        #f.grid(row=0, column=1, sticky="nsew")

        # no need to pack since we using grid geometry
        # f.pack(fill=tk.Y,expand=-1,side = tk.LEFT)

        # Create/Format table
        #table = TableCanvas(f, cellwidth=60, data = test, cellbackgr='white', thefont=('Arial',12),rowheight=25, rowheaderwidth=30, rowselectedcolor='yellow', editable=True)

        #Import table from csv
        #table.importCSV('2017_Traffic_Volume_Flow.csv')

        """if importing table as dictionary, use this: data is of type dictionary
        """
        # table = TableCanvas(f, cellwidth=60, data = data, cellbackgr='white',
        #                    thefont=('Arial', 12), rowheight=25, rowheaderwidth=30,
        #                    rowselectedcolor='yellow', editable=True)

        #print (table.model.columnNames)
        #table.show()
        # sort the first column from highest to lowest (the sum of incident column)
        # table.sortTable(reverse=1)

        return

    def importData(self, dataImport):
        data = dataImport
        model = TableModel()
        model.importDict(data)
        f = Frame(self.main)
        self.table = TableCanvas(f, model, cellwidth=60, cellbackgr='white', thefont=('Arial',12),rowheight=25, rowheaderwidth=30, rowselectedcolor='yellow', editable=True)
        self.table.createTableFrame()
        self.table.show()
        f.grid(row=0, column=1, sticky="nsew")

    def sortData(self,l):
        self.table.sortTable(reverse=l)
        self.table.redraw()


# window = tk.Tk()
# window.title("Don and Sarim beast project")
# test = App(window)
# test.importData(testing)
# test.pack()
# window.mainloop()


