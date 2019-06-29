import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

import sys

class MyWindow(Gtk.Window):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./form.glade')
        
        self.builder.connect_signals(self) #aClassThatHandlerSignals, it is
        
        self.window = self.builder.get_object('Form1')
        self.window.show()
    
    # Signals
    def onQuit(self, *a, **kv):
        print('Goobye')
        sys.exit()
    def onClicked(self, *a, **kv):
        print('Button clicked')
        

if __name__ == '__main__':
    win = MyWindow()
    Gtk.main()