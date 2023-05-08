from flask import Flask


SECRET_KEY = 'fgnlfbgkmdldkfgnfgknf'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    return app