from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

root = Tk()
root.title("text editor on BIDDY")
root.geometry("300x300")



custom_font = ("Helvetica", 16, "bold")
def savetext():
  text = scrolledtext.get("1.0", tk.END)
  with open('demofile.txt', 'w') as f:
    f.write(text)

text_area = scrolledtext.ScrolledText(root,
                                      wrap = WORD,
                                      width = 40,
                                      height = 10,
                                      font = ("Times New Roman",
                                              15))

savename = ttk.Entry(root, width=20, font=("Helvetica", 12)) 
save = ttk.Button(
  root,
  width = 1.5,
  text="save"
  ,command=savetext)
save.place(x=25,y=175)


openbutton = ttk.Button(root, width =1.5, text="open")
openbutton.place(x = 225,y=175)

text_area.pack()
savename.pack()
root.mainloop()
