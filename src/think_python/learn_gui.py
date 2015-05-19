#!/usr/bin/python

from Gui import *

def make_button():
    g.bu(text="New button created", command=make_label)

def make_label():
    g.la(text="Well done!")

g = Gui()
g.title("Gui")
button = g.bu(text="Creat new button", command=make_button)
g.mainloop()


