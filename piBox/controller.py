
from flask import Blueprint, render_template
from model import home, music, videos, browser, documents, files

mod = Blueprint('index', __name__)

@mod.route('/')
def show_index():
  return render_template('index.html')

@mod.route('/music/')
def show_music():
  return render_template('music.html')

@mod.route('/videos/')
def show_videos():
  return render_template('videos.html')

@mod.route('/browser/')
def show_browser():
  return render_template('browser.html')

@mod.route('/documents/')
def show_documents():
  return render_template('documents.html')

@mod.route('/files/')
def show_files():
  return render_template('files.html')