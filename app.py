from flask import Flask, render_template
from db import *
import os
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        pass
    else:
        pass
    return render_template("index.html")

@app.route('/<name>')
def redirect(name):
    coll = get_collection()
    close_db()
    return 'This page will redirect to an actual URL.'