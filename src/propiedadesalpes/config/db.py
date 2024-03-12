from flask_sqlalchemy import SQLAlchemy
from flask import Flask

def init_db(app: Flask):
    global db
    db = SQLAlchemy(app)
