from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

root = Tk()
root.title("text editor on BIDDY")
root.geometry("300x300")

text_area = scrolledtext.ScrolledText(root,
                                      wrap = WORD,
                                      width = 40,
                                      height = 10,
                                      font = ("Times New Roman",
                                              15))

text_area.pack()
root.mainloop()