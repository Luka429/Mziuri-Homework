from flask import Flask

app = Flask(__name__)

@app.route("/calculate/<int:x>/<int:y>/<int:z>/<string:operation>")
def calculator(x,y,z,operation):
    result = None
    if operation == "+":
        result = x + y + z
    elif operation == "-":
        result = x - y - z
    elif operation == "*":
        result = x * y * z
    elif operation == ":":
        if y and z != 0:
            result = x / y / z
        else:
            return "<h2>Division by zero error</h2>"
    elif result is None:
        return "<h2>invalid arguments</h2>"
    return f"<h2>{result}</h2>"

if "__main__" == __name__:
    app.run()
