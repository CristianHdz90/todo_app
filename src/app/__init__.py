from flask import Flask
from .blueprints.auth import auth
from flask_login import LoginManager
from .models import UserModel
from .config import Config


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
