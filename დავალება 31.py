from flask import Flask

app = Flask(__name__)

@app.route("/register")
def register():
    return "<h2>Register</h2>"

@app.route("/login")
def login():
    return "<h2>Login</h2>"

@app.route("/profile")
def profile():
    return "<h2>Profile</h2>"

if __name__ == "__main__":
    app.run()
