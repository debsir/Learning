#!/usr/bin/python

import pygtk
import gtk
import time

class SimpleButtonApp(object):
    """This is a simple PyGTK app that has only one window and one button.
    When the button is clicked, it updates the button's label with current time.
    """

    def __init__(self):
        #The main window of the application
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        #This is how you "register" an event handler. Basically, this
        #tells the gtk main loop to call self.quit() when the window 
        #"emits" the "destroy" signal.
        self.window.connect("destroy", self.quit)

        #A button labeled "Click Me"
        self.button = gtk.Button("Click Me")

        #Another registration of an event handler. This time, when the
        #button "emits" the "clicked" signal, the "update_button_label"
        #method will get called.
        self.button.connect("clicked", self.update_button_label, None)

        #The window is a container. The "add" method puts the button
        #inside the window.
        self.window.add(self.button)

        #This call makes the button visable, but it won't become visible
        #until its container becomes visible as well.
        self.button.show()

        #Makes the container visible
        self.window.show()

    def update_button_label(self, widget, data=None):
        """Set the button label to the current time

        This is the handler method for the "clicked" event of the button
        """
        self.button.set_label(time.asctime())

    def quit(self, widget, data=None):
        """Stop the main gtk event loop
        When you close the main window, it will go away, but if you don't
        tell the gtk main event loop to stop running, the application will 
        continue to run even though it will look like nothing is really
        happening.
        """
        gtk.main_quit()


    def main(self):
        """Start the gtk main event loop"""
        gtk.main()

if __name__ == "__main__":
    s = SimpleButtonApp()
    s.main()
















































