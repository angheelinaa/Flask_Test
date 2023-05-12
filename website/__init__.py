from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy


SECRET_KEY = 'fgnlfbgkmdldkfgnfgknf'
DB_NAME = "database.db"

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from .model import Note

    with app.app_context():
        db.create_all()

    return app


# def create_database(app):
#     if not path.exists(f"website/{DB_NAME}"):
#         db.create_all(app=app)
#         print("Создана новая база данных")