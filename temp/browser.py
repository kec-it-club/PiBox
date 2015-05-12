#!/usr/bin/python2

import gtk
import webkit

def main():
  window = gtk.Window()
  webview = webkit.WebView()
  webview.load_uri("https://google.com")
  window.add(webview)
  window.show_all()
  gtk.main()

if __name__=='__main__':
  main()
