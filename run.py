import os
from flask import Flask #Capital F implies it is a class and so is important

app = Flask(__name__) # Creating an instance of Class Flask 


@app.route("/") #decorator
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT","5000")),
        debug = True)