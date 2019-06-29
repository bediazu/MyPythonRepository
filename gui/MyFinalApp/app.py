# brunodiazu

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

from MyWindow import Window

# ANOTHER IMPORTS
import sys

# MAIN
if __name__ == '__main__':
    win = Window()
    Gtk.main()
