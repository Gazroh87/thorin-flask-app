import os
import json
from flask import Flask, render_template, request, flash
# Importing Flask class
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
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
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        "about.html", pge_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # print(request.form.get("name"))
        # print(request.form["email"])
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", pge_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", pge_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# debug should bet set to False in a production app or when submitting projects
