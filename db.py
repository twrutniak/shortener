from flask import current_app, g
from os import getenv
import pymongo

def get_db():
    if 'db' not in g:
        g.db = pymongo.MongoClient(getenv("MONGO_HOST"), int(getenv("MONGO_PORT"))) 
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def get_collection():
    db = get_db()
    collection = db.urldb.urlcollection
    return collection