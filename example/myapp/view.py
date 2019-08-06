from flask import Flask
from myapp import db
import requests
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from myapp.models import Users,Todos,Albums,Comments,Posts,Photos
db.create_all()

#Fetching user data 
fetch_data = requests.get("https://jsonplaceholder.typicode.com/users")
data = fetch_data.json()
for record in data:
    fetch = Users(id=record['id'], name=record['name'], username=record['username'],
                  email=record['email'], phone=record['phone'], website=record['website'], address=record['address'])
    db.session.add(fetch)
    db.session.commit()

#Fetchinf todos data
fetch_todos_data = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = fetch_todos_data.json()
for record in todos:
     todos_data = Todos(userId=record['userId'], id=record['id'],
                 title=record['title'], completed=record['completed'])
     db.session.add(todos_data)
     db.session.commit()

#Fetching album data
fetch_album_data = requests.get("https://jsonplaceholder.typicode.com/albums")
album = fetch_album_data.json()
for record in album:
    album_data = Albums(userId=record['userId'],
                 id=record['id'], title=record['title'])
    db.session.add(album_data)
    db.session.commit()

#Fetching comments data
fetch_comments_data = requests.get("https://jsonplaceholder.typicode.com/comments")
comments = fetch_comments_data.json()
for record in comments:
    comments_data = Comments(postId=record['postId'], id=record['id'], name=record['name'],
                    email=record['email'], body=record['body'])
    db.session.add(comments_data)
    db.session.commit()

#Fetching posts data
fetch_posts_data = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = fetch_posts_data.json()
for record in posts:
    posts_data = Posts(userId=record['userId'], id=record['id'], 
                title=record['title'], body=record['body'])
    db.session.add(posts_data)
    db.session.commit()
  
#Fetching Photos data
fetch_photos_data = requests.get("https://jsonplaceholder.typicode.com/photos")
photos = fetch_photos_data.json()
for record in photos:
    photos_data = Photos(albumId=record['albumId'], id=record['id'], 
                  title=record['title'], thumbnailUrl=record['thumbnailUrl'])
    db.session.add(photos_data)
    db.session.commit()

