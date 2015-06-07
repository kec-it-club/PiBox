#!/usr/bin/python

from flask import Flask, render_template
import threading

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
  return "404: Page not found.", 404

@app.route('/')
def index():
  return "Welcome to <b>piBox</b><br>Sorry, we are still under construction. \
    <a href=\"https://google.com\">Go to Google for now.</a>"

if __name__=='__main__':
  app.run(debug=True)
