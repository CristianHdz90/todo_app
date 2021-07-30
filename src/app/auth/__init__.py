from flask import Blueprint


auth = Blueprint('auth', __name__, url_prefix='/auth')

#Import the endpoints file
from . import views