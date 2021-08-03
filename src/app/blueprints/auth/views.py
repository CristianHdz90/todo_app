from flask import render_template, request, redirect, url_for
from . import auth


@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':

        user = request.form['nm']
        return redirect( url_for('auth.user_name', user = user))
    else:
        return render_template('login.html')
    
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@auth.route('/<user>')
def user_name(user):
    return f'<h1>Hola {user}</h1>'