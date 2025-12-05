from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
green_button = Button(root, text="green", background='green')
yellow_button = Button(root, text="yellow", background='yellow')

#Add a label
label = Label(root, text="CHANGE ME!")

# Place widgets in window (with pack function!)
label.pack()
red_button.pack()
green_button.pack()
yellow_button.pack()

# Start the GUI event loop
root.mainloop()

