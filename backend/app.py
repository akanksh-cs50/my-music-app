from flask import Flask, request
import os
import json

app = Flask(__name__)

# Configuration (Change as per your needs)
app.config['music_directory'] = '/home/akanksh/Music/'

@app.route("/songs")
def songs():
"""
when returning the songs, it's better to send them back as an entire object, like a song object, with name, album, artists, filepath
"""
    pass 

@app.route("/artists")
def songs():
    pass

@app.route("/albums")
def songs():
    pass

@app.route("/search")
def songs():
    pass
