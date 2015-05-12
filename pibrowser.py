#!/usr/bin/python2

import gtk
import webkit
import piremote
import sys

class Browser(gtk.Window):

  def __init__(self,url):
    gtk.Window.__init__(self)

    webview = webkit.WebView()
    webview.load_uri(url)

    self.add(webview)

    self.set_title("Starting now")
    self.connect("destroy",self.destroy)

    self.remotethread()

    self.show_all()

  def remotethread(self):
    remote = piremote.Remote(self)
    remote.daemon = True
    remote.start()

  def destroy(self,widget,data=None):
    gtk.main_quit()

if __name__=='__main__':
  if len(sys.argv) == 2:
    url = sys.argv[1]
  else:
    url = "https://google.com"

  win = Browser(url)
  gtk.gdk.threads_init()
  gtk.gdk.threads_enter()
  gtk.main()
  gtk.gdk.threads_leave()
