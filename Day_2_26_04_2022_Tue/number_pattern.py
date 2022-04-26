#importing packages
import time
from datetime import datetime
import os
import pyautogui
import tkinter
from tkinter import filedialog
from tkinter import *

#Tkinter window withdrawl
root = Tk()
root.withdraw()
# folder selection
folder_selected = filedialog.askdirectory()

num_of_rows=int(input("number of rows :"))

for counter_row in range(1,num_of_rows+1):
    for space in range(num_of_rows-counter_row):
        print(" ",end='')
    for symbol_print in range(1,counter_row+1):
        print("*",end=" ")
    print()
current_time= datetime.now()
format="%y_%b_%d_%H_%M_%S"
current_time=datetime.strftime(current_time,format) #convert timestamp data to string presented in the above format
location=os.path.join(folder_selected,"num_of_rows{}_{}.jpeg".format(num_of_rows,current_time))
myScreenshot = pyautogui.screenshot()
myScreenshot.save(location)


