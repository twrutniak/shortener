from flask import Flask, render_template, request, redirect, url_for
from secrets import token_urlsafe
from os import getenv
from re import sub
from db import *

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        url = re.sub("^http.*://", "", str(request.form["url"]))
        env = getenv("TOKEN_NBYTES")
        if env is not None:
            token = token_urlsafe(int(getenv("TOKEN_NBYTES")))
        else:
            token = token_urlsafe(4)
        coll = get_collection()
        coll.insert_one({"url":url, "token":token})
        close_db()
        return render_template("index.html", passed=token)
    else:
        return render_template("index.html")

@app.route('/<token>')
def redirect(token):
    coll = get_collection()
    doc = coll.find_one({"token":str(token)})
    close_db()
    try:
        doc["ads"]
        timeout = getenv("ADS_REDIRECT_TIMEOUT")
        if timeout is not None:
            return render_template("ads.html", timeout=int(timeout))
        else:
            return render_template("ads.html", timeout=5)
    except KeyError as E:
        return redirect(str(doc["url"]))