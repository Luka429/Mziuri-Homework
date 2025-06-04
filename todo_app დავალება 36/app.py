from flask import Flask, render_template, request, redirect, url_for
from database import read, init_db, create, delete, update

app = Flask(__name__)

@app.route("/")
def main():
     data = read()
     return render_template("main.html", todos = data)

@app.route("/add", methods=["POST"])
def add_todo():
    todo_title = request.form["todo_title"]
    todo_text = request.form["todo_text"]

    create(todo_title, todo_text)
    return redirect(url_for("main"))

@app.route("/delete/<int:pk>", methods=["POST"])
def delete_todo(pk):
    delete(pk)
    return redirect(url_for("main"))

@app.route("/update/<int:pk>" , methods=["POST"])
def update_todo(pk):
    new_title = request.form["new_title"]
    new_text = request.form["new_text"]
    update(pk,new_title,new_text)
    return redirect(url_for("main"))


    

if __name__ == '__main__':
    init_db()
    app.run(debug=True)