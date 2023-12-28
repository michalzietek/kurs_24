from flask import render_template, Blueprint

paths = Blueprint("routes", __name__)


@paths.route("/")
def index():
    return render_template("main.html")


@paths.route("/about")
def about():
    return render_template("about.html")