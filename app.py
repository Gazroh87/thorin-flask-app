import os
from flask import Flask
# Importing Flask class


app = Flask(__name__)
"""
Creating an instance of the Flask class and storing it
in a variable called app. The first argument of the class
is the name of the application's module - our package.
Since we're just using a single module, we can use __name__
which is a built-in Python variable. Flask needs this so
that it knows where to look for templates and static files.
"""


@app.route("/")
# Using app.route decorator for wrapping functions.
# When we try to browse the root directory, then Flask
# triggers the index function underneath and returns the
# "Hello, World" text.
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# debug should bet set to False in a production app or when submitting projects
