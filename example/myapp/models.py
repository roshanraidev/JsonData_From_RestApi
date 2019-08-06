from flask import Flask
from myapp import db
import requests

class Users(db.Model):
    id = db.Column(db.Integer)
    name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20), primary_key=True)
    website = db.Column(db.String(50))
    address = db.Column(db.String(50))

class Todos(db.Model):
    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    completed = db.Column(db.String(10))

class Albums(db.Model):
    userId = db.Column(db.Integer)
    id = db.Column(db.Integer)
    title = db.Column(db.String(80), primary_key = True)

class Comments(db.Model):
    postId = db.Column(db.Integer)
    id = db.Column(db.Integer)
    name = db.Column(db.String(80))
    email = db.Column(db.String(60),primary_key = True)
    body = db.Column(db.String(60))

class Posts(db.Model):
    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(60))

class Photos(db.Model):
    albumId = db.Column(db.Integer)
    id = db.Column(db.Integer)
    title = db.Column(db.String(80))
    thumbnailUrl = db.Column(db.String(50), primary_key = True)

from myapp import view

