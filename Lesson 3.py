from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
wind=Tk()
wind.title("Menu")

#creating menubar
menubar=Menu(wind)

#Adding a file menu and commands
file=Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=None)
file.add_command(label="Open", command=None)
file.add_command(label="Save", command=None)
file.add_separator()
file.add_command(label="Exit", command=wind.destroy)

#Adding a edit menu and commands
edit=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut", command=None)
edit.add_command(label="Copy", command=None)
edit.add_command(label="Paste", command=None)
edit.add_command(label="Select All", command=None)
edit.add_separator()
edit.add_command(label="Find", command=None)
edit.add_command(label="Find Again", command=None)

#Adding a help menu and commands
help=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="Tk Help", command=None)
help.add_command(label="Demo", command=None)
help.add_separator()
help.add_command(label="About Tk", command=None)

#display Menu
wind.config(menu=menubar)
mainloop()