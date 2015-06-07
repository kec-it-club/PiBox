#!/usr/bin/python

from gi.repository import Gtk, WebKit, Gdk
import threading
import piremote

class Browser(Gtk.Window):

  def __init__(self,url):
    Gtk.Window.__init__(self)

    webview = WebKit.WebView()
    webview.load_uri(url)

    self.add(webview)

    self.connect("destroy",self.destroy)

    self.remotethread()

    self.set_default_size(800,600)
    self.set_decorated(False)
    self.maximize()
    #self.fullscreen()

    self.show_all()

  def remotethread(self):
    remote = piremote.Remote(self)
    remote.daemon = True
    remote.start()

  def destroy(self,widget,data=None):
    Gtk.main_quit()

if __name__=='__main__':
  url = "http://localhost:5000"
  #url = "http://google.com"

  win = Browser(url)
  Gdk.threads_init()
  Gdk.threads_enter()
  Gtk.main()
  Gdk.threads_leave()
