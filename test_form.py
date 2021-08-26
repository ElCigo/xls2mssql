from tkinter import *

root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Jebem ti mater?")
label.pack()
root.mainloop()


