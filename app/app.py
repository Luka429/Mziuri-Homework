from flask import Flask
import database


app = Flask(__name__)

users = []

    
@app.route("/register/<username>/<password>")
def register_user(username,password):
    database.register(username,password)
    

@app.route("/login/<username>/<password>")
def login_user(username,password):
    database.login(username,password)


@app.route("/users") 
def get_users():
    database.users_get()
    
@app.route("/users/<int:id>")
def get_user(id):
    database.user_get(id)

@app.route("/delete/<int:id>")
def delete_user(id):
    database.delete(id)


@app.route("/update/<int:id>/<username>/")
def update_username(id,username):
    database.update(id,username)

if __name__ == "__main__":
    app.run(debug=True)