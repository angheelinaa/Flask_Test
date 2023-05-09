from flask import Blueprint


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return '<H1> THIS IS HOME PAGE </H1>'


@views.route('/notes')
def notes():
    return '<H1> THIS IS PAGE FOR MY NOTES </H1>'