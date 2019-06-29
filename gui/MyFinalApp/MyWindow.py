import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

import sys

class Window(Gtk.Window):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./form1.glade')
        
        self.builder.connect_signals(self)
        
        self.window = self.builder.get_object('Form1')
        self.window.show()
        
    def onQuit(self, *a, **kv):
        sys.exit()
    def onClicked(self, button):
        print('Button clicked')