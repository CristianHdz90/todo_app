import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY_FLASK')
    # SECRET_KEY = 'YMrrFMaSWM6Ykntf=9LBpeWZ#tWzK-Rawy64gsjTEh@z3z+H8tNw5c&3YpMa'