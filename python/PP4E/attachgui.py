#!/usr/bin/env python3

from tkinter import *
from tkinter102 import MyGui

# main app window
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# popup window
popup = Toplevel()
Label(popup, text='Attach').pack(side=RIGHT)
MyGui(popup).pack(side=LEFT)
mainwin.mainloop()


