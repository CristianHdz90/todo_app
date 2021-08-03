from flask import Blueprint


auth = Blueprint('auth', __name__,
                url_prefix='/auth',
                static_folder='static',
                template_folder='templates')


#Import the endpoints file
from . import views