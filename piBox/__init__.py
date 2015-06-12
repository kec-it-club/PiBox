#!/usr/bin/python

from flask import Flask, render_template
import controller

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
  return "404: Page not found.", 404

app.register_blueprint(controller.mod)

if __name__=='__main__':
  app.run(debug=True)
