#!/usr/bin/python
"""
This module will start the Gtk window with a webkit frame within. It will load
the default Flask website (http://localhost:5000)
"""

from gi.repository import Gtk, WebKit, Gdk
import threading, sys
import piremote

class Browser(Gtk.Window):

  def __init__(self,url):
    
    def title_changed(widget, frame, title):
      self.isBrowser = False
      if title != 'null':
        uri = self.webview.get_uri()
        if uri.split('/')[-2] == 'browser':
          self.addressBox.show()
          self.address.set_text('https://duckduckgo.com')
          self.webview.load_uri('https://duckduckgo.com')
          return
        elif uri.split('/')[2].split(':')[0] in ['localhost','127.0.0.1']:
          self.addressBox.hide()

        self.address.set_text(self.webview.get_uri())
        self.set_title(title)

    def loading(widget, frame, data='Start'):
      if 'loadingSpinner' not in locals(): return
      if data=='Start':
        loadingSpinner.start()
        loadingSpinner.show()
      elif data=='Stop':
        loadingSpinner.stop()
        loadingSpinner.hide()

    def addressKeyPress(widget, ev='', data=None):
      if widget == self.address and ev.keyval == Gdk.KEY_Return:
        add = self.address.get_text()
        if add.split('://')[0] in ['http','https']:
          self.webview.load_uri(add)
        elif add.lower() in ['home','music','browser']:
          if add.lower() == 'home':
            self.webview.load_uri(url)
          else:
            self.webview.load_uri(url+'/'+add.lower())
        else:
          self.webview.load_uri('http://'+add)

    def navBtnClick(widget, data=None):
      if widget == goBack:
        lastItem = self.webview.get_back_forward_list().get_back_item().get_uri()
        if lastItem.split('/')[-2] == 'browser':
          self.webview.go_back_or_forward(-2)
          return
        self.webview.go_back()

      elif widget == goForward:
        self.webview.go_forward()

      elif widget == goHome:
        self.webview.load_uri(url)

    Gtk.Window.__init__(self)

    self.mainBox = Gtk.VBox()

    scrolledWindow = Gtk.ScrolledWindow()

    self.webview = WebKit.WebView()
    self.webview.connect('title-changed', title_changed)
    self.webview.connect('load-started', loading, 'Start')
    self.webview.connect('load-finished', loading, 'Stop')
    self.webview.load_uri(url)

    scrolledWindow.add(self.webview)

    self.addressBox = Gtk.HBox()
    #self.addressBox.set_spacing(5)

    goBack = Gtk.Button()
    goBack.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_GO_BACK, 0))
    goBack.connect("clicked", navBtnClick)

    goForward = Gtk.Button()
    goForward.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_GO_FORWARD, 0))
    goForward.connect("clicked", navBtnClick)

    self.address = Gtk.Entry()
    self.address.connect("key-press-event", addressKeyPress)

    goBtn = Gtk.Button()
    goBtn.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_OK, 0))
    goBtn.connect("clicked", addressKeyPress)

    goHome = Gtk.Button()
    goHome.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_HOME, 0))
    goHome.connect("clicked", navBtnClick)

    loadingSpinner = Gtk.Spinner()

    self.addressBox.pack_start(goBack, False, False, 0)
    self.addressBox.pack_start(goForward, False, False, 0)
    self.addressBox.pack_start(self.address, True, True, 0)
    self.addressBox.pack_start(loadingSpinner, False, False, 0)
    self.addressBox.pack_start(goBtn, False, False, 0)
    self.addressBox.pack_start(goHome, False, False, 0)

    self.mainBox.pack_start(self.addressBox, False, False, 5)

    self.mainBox.pack_end(scrolledWindow, True, True, 0)
    
    self.add(self.mainBox)

    self.connect("destroy",self.destroy)

    self.remotethread()

    self.set_default_size(800,600)
    self.set_decorated(True)
    
    if 'f' in sys.argv:
      self.fullscreen()
    elif 'w' in sys.argv:
      pass
    else:
      self.maximize()

    self.show_all()
    self.addressBox.hide()
    loadingSpinner.hide()

  def remotethread(self):
    remote = piremote.Remote(self)
    remote.daemon = True
    remote.start()

  def destroy(self,widget,data=None):
    Gtk.main_quit()

if __name__=='__main__':
  url = "http://localhost:5000"

  win = Browser(url)
  Gdk.threads_init()
  Gdk.threads_enter()
  Gtk.main()
  Gdk.threads_leave()
