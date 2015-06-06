#!/usr/bin/python

from flask import Flask, render_template
import threading

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return "404: Page not found"

class flaskThread(threading.Thread):
  def run(self):
    app.run()

def start():
  flask = flaskThread()
  flask.daemon = True
  flask.start()
  

if __name__=='__main__':
  app.run(debug=True)
