from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.confid['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    password = db.Columt(db.String(30))

class post(db.model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(150))
    username = db.Columt(db.string(100), db.ForeignKey('User.username'))

@app.route("/add_post", methods =["GET", "POST"])
def add_post():
    if request.method == "POST":
        description = request.form["description"]
        username = request.form["username"]
        new_post = post(description=description, username=username)
    
    for User_username in User:
        if User_username:
            existing_username = User.query.filter_by(username=User_username).first()
            if existing_username:
                post.username.append(existing_username)
            else:
        
