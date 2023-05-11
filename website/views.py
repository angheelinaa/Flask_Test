from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/notes')
def notes():
    return '<H1> THIS IS PAGE FOR MY NOTES </H1>'