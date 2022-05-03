import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import *
from tkHyperlinkManager import HyperlinkManager
from functools import partial
# Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)
LARGEFONT = ("Verdana", 35)

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1920x1080")
        #=StringVar()
        #y=StringVar()
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=1)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (DbHome, DBOperation, Architecture,DML_examples,Update,Delete,Select,Insert,oracle,mongodb):
            frame = F(container, self)

            # initializing frame of that object from
            # DbHome, DBOperation, Architecture respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(DbHome)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame DbHome

class DbHome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="DB HOME", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=15, pady=15)

        button1 = ttk.Button(self, text="MYSQL DB OPERATION",
                             command=lambda: controller.show_frame(DBOperation),width=25)

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=0, padx=15, pady=15)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Architecture Details",
                             command=lambda: controller.show_frame(Architecture),width=25)
        button2.place(width=50, height=50)

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=0, padx=15, pady=15)
        button3 = ttk.Button(self, text="Oracle DB Operation",
                             command=lambda: controller.show_frame(oracle),width=25)
        button3.place(width=50, height=50)
        # putting the button in its place by
        # using grid
        button3.grid(row=3, column=0, padx=15, pady=15)
        button4 = ttk.Button(self, text="Mongo DB DB Operation",
                             command=lambda: controller.show_frame(mongodb),width=25)
        button4.place(width=50, height=50)
        # putting the button in its place by
        # using grid
        button4.grid(row=4, column=0, padx=15, pady=15)


# second window frame DBOperation
class DBOperation(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="DB Operation", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="DB HOME",
                             command=lambda: controller.show_frame(DbHome),width=25)

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=0, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Architecture Details",
                             command=lambda: controller.show_frame(Architecture),width=25)

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=0, padx=10, pady=10)
        button2 = ttk.Button(self, text="DML_examples",
                             command=lambda: controller.show_frame(DML_examples),width=25)

        # putting the button in its place by
        # using grid
        button2.grid(row=4, column=0, padx=10, pady=10)
class Update(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Update", font=LARGEFONT)
        label.grid(row=1, column=0, padx=10, pady=10)
        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(DML_examples))

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=0, padx=10, pady=10)
        content = '''UPDATE <table_name> SET <column_name = value>\nWHERE condition;\nEx:UPDATE students
SET due_fees = 20000 WHERE stu_name = 'Mini'; '''
        label = ttk.Label(self, text=content, font=("Courier", 20))
        label.grid(row=3, column=1)
class Delete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Delete", font=LARGEFONT)
        label.grid(row=1, column=0, padx=10, pady=10)
        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(DML_examples))

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=0, padx=10, pady=10)
        content = '''DELETE FROM <table_name> WHERE <condition>;\nDELETE FROM students\n WHERE stu_id = '001'; '''
        label = ttk.Label(self, text=content, font=("Courier", 20))
        label.grid(row=3, column=1)
class Select(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select", font=LARGEFONT)
        label.grid(row=1, column=0, padx=10, pady=10)
        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(DML_examples))

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=0, padx=10, pady=10)
        content = '''SELECT Col1, Col2, Col3  FROM  table_name\nCol1, Col2, Col3  = (is the column name from which data is retrieved.)\n
table_name = is the name of table from which the data is retrieved. '''
        label = ttk.Label(self, text=content, font=("Courier", 20))
        label.grid(row=3, column=1)

class Insert(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Insert", font=LARGEFONT)
        label.grid(row=1, column=0, padx=10, pady=10)
        content = '''INSERT INTO table_name (column1, column2, column3, ...)\nVALUES (value1, value2, value3, ...);'''
        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(DML_examples))

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=0, padx=10, pady=10)
        label = ttk.Label(self, text=content, font=("Courier", 20))
        label.grid(row=3, column=1)
        link1 = Label(controller, text="Google Hyperlink", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind(lambda e: callback("http://www.google.com"))



class DML_examples(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="DML_examples", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Insert",
                             command=lambda: controller.show_frame(Insert))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Update",
                             command=lambda: controller.show_frame(Update))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)
        button3 = ttk.Button(self, text="Delete",
                             command=lambda: controller.show_frame(Delete))

        # putting the button in its place
        # by using grid
        button3.grid(row=4, column=1, padx=10, pady=10)
        button4= ttk.Button(self, text="Select",
                             command=lambda: controller.show_frame(Select))

        # putting the button in its place
        # by using grid
        button4.grid(row=6, column=1, padx=10, pady=10)
        button5 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(DbHome))

        # putting the button in its place by
        # using grid
        button5.grid(row=7, column=0, padx=10, pady=10)
# third window frame Architecture
class Architecture(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Architecture Details", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        content="1)SQL Access LDAP,2)thread,3)QUery)"
        label = ttk.Label(self, text=content, font=("Courier", 20))
        label.grid(row=3, column=1)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="DB OPERATIONS",
                             command=lambda: controller.show_frame(DBOperation),width=25)

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="DB HOME",
                             command=lambda: controller.show_frame(DbHome),width=25)

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

class oracle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Yet to be configured !!! Stay tuned for updates", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(DbHome))

        # putting the button in its place by
        # using grid
        button2.grid(row=1, column=0, padx=10, pady=10)
class mongodb(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Yet to be configured !!! Stay tuned for updates", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)
        button2 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(DbHome))

        # putting the button in its place by
        # using grid
        button2.grid(row=1, column=0, padx=10, pady=10)
# Driver Code
if __name__ == '__main__':
    app = tkinterApp()
    app.mainloop()
