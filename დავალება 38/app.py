from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(30))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(150))
    username = db.Column(db.String(100), db.ForeignKey('User.username'))

@app.route("/add_post", methods =["GET", "POST"])
def add_post():
    if request.method == "POST":
        description = request.form["description"]
        username = request.form["username"]
        new_post = Post(description=description, username=username)
    
    for User_username in User:
        if User_username:
            existing_username = User.query.filter_by(username=User_username).first()
            if existing_username:
                Post.username.append(existing_username)
                return "successfully posted"
            else:
                return redirect(url_for('login'))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return("username is already taken choose another one")
            
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return redirect(url_for('add_post')) 

        return redirect(url_for('login'))

    
