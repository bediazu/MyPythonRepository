import gi
import sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

Whatis = lambda obj : print(type(obj),"\n\t"+"\n\t".join(dir(obj)))

class aClassThatHandleGtkSignals:
    def onQuit(self,*a,**kv):
        print('Goodbye')
        sys.exit()

def init_form():
    abuilder = Gtk.Builder()
    abuilder.add_from_file('./form.glade')
    abuilder.connect_signals(aClassThatHandleGtkSignals)
    ourForm1 = abuilder.get_object('Form1')
    ourForm1.show()
    Gtk.main()


if __name__ == '__main__':
    init_form()

