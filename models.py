import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite?check_same_thread=False"))  # this connects to a database either on Heroku or on localhost


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)  # a username must be unique! Two users cannot have the same username
    email = db.Column(db.String, unique=True)  # email must be unique! Two users cannot have the same email address
    secret_number = db.Column(db.Integer, unique=False)  # must NOT be unique across user objects
    password = db.Column(db.String)
    session_token = db.Column(db.String)

class Message(db.Model):
        messageID = db.Column(db.Integer, primary_key=True)
        sender = db.Column(db.Integer)
        receiver = db.Column(db.Integer)
        messageBody = db.Column(db.String)