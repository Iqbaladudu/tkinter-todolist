from tkinter import *

main = Tk()
var1 = IntVar()
Checkbutton(main, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(main, text='male', variable=var2).grid(row=1, sticky=W)

mainloop()