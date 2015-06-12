#!/usr/bin/python
""" piRemote
This module will handle all the communication with the remote and pass signals
to the main Gtk window using the GLib.idle_add() function.
"""

import threading
import time
from gi.repository import GLib

class Remote(threading.Thread):

  def __init__(self, window):
    threading.Thread.__init__(self)
    self.window = window

  def run(self):
    for i in range(5,0,-1):
      time.sleep(1)
      GLib.idle_add(self.settitle,i)
    GLib.idle_add(self.settitle,'piBox')

  def settitle(self,i):
    self.window.set_title(str(i)) 
