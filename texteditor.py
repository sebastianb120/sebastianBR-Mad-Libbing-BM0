 from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("Text editor")

root.geometry("150x350")


#video being used https://www.youtube.com/watch?v=0WafQCaok6g
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
