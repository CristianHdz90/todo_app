from .blueprints.auth import auth
from .config import Config
from flask import Flask
from flask_login import LoginManager
from .models import UserModel


login_manager = LoginManager()
login_manager.login_view = 'auth.login' 

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query(user_id)


def create_app():

    app = Flask(__name__)

    login_manager.init_app(app)
    app.register_blueprint(auth)
    app.config.from_object(Config)

    return app
