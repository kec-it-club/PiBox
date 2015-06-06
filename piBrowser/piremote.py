#!/usr/bin/python

import threading
import time
from gi.repository import GLib

class Remote(threading.Thread):

  def __init__(self, window):
    threading.Thread.__init__(self)
    self.window = window

  def run(self):
    for i in range(10):
      time.sleep(1)
      GLib.idle_add(self.settitle,i)
    GLib.idle_add(self.settitle,'Done with the counting')

  def settitle(self,i):
    self.window.set_title(str(i)) 
