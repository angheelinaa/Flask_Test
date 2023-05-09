from flask import Blueprint


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return '<H1> THIS IS PAGE LOGIN</H1>'


@auth.route('/register')
def register():
    return '<H1> THIS IS PAGE REGISTER </H1>'


@auth.route('/logout')
def logout():
    return '<H1> THIS IS PAGE LOGOUT </H1>'