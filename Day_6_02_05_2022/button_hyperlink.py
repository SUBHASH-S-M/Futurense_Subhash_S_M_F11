# Import the required libraries
from tkinter import *
from tkHyperlinkManager import HyperlinkManager
import webbrowser
from functools import partial

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")

# Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

# Create a Label to display the link
text = Text(win)
text.insert(END,"Click here for demo ")
text.pack()
hyperlink= HyperlinkManager(text)

text.insert(END,
"TutorialsPoint",hyperlink.add(partial(webbrowser.open,"http://www.tutorialspoint.com")))

win.mainloop()