from . import db
from sqlalchemy import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), default=func.now())
    text = db.Column(db.String(1000))