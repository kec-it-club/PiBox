#!/usr/bin/python2

import threading
import time
import gobject
import gtk

class Remote(threading.Thread):

  def __init__(self, window):
    threading.Thread.__init__(self)
    self.window = window

  def run(self):
    for i in range(10):
      time.sleep(1)
      gobject.idle_add(self.settitle,i)
    gobject.idle_add(self.settitle,'Done with the counting')

  def settitle(self,i):
    self.window.set_title(str(i)) 
