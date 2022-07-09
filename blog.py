from flask import Flask

from datetime import datetime

from sqlalchemy import null


def create_post_model(db):
    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        date = db.Column(db.DateTime, default=datetime.now)
        text = db.Column(db.String, nullable=False)
    return Post



