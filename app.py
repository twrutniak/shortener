from flask import Flask, render_template, request, redirect, url_for
from secrets import token_urlsafe
from db import close_db, get_collection
from os import getenv
from re import sub


app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        url = sub("^http.*://", "", str(request.form["url"]))
        coll = get_collection()
        if coll.find_one({"url":url}) is not None:
            token = coll.find_one({"url":url})["token"]
        else:
            nbytes = getenv("TOKEN_NBYTES")
            if nbytes is not None:
                token = token_urlsafe(int(getenv("TOKEN_NBYTES")))
            else:
                token = token_urlsafe(4)
            if getenv("ADS") is not None:
                coll.insert_one({"url":url, "token":token, "ads":True})
            else:
                coll.insert_one({"url":url, "token":token})
        close_db()
        return render_template("index.html", token=token)
    else:
        return render_template("index.html")

@app.route('/<string:token>', methods=["GET"])
def direct(token):
    coll = get_collection()
    doc = coll.find_one({"token":str(token)})
    close_db()
    if doc is None:
        return redirect(url_for("index"))
    if 'ads' in doc:
        timeout = getenv("ADS_REDIRECT_TIMEOUT")
        if timeout is not None:
            return render_template("ads.html", timeout=int(timeout))
        else:
            return render_template("ads.html", timeout=5)
    else:
        return redirect("http://" + str(doc["url"]))