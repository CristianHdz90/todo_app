from flask import Flask
from .blueprints.auth import auth


def create_app():

    app = Flask(__name__)
    app.register_blueprint(auth)

    return app
