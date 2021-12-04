# Importing all files needed to generate the UI for the application
from tkinter import *
# Initializing the application
root = Tk()
# Setting the application name to `the long game.`
root.title("the long game.")
# Setting the application window size to 100x30px
root.geometry('100x30')
# Disabling application window resize
root.resizable(0,0)
# Adding text in the application window
label = Label(root, text='deez nuts').pack()
# Looping the processes so that the application will not close immediately when opened
mainloop()