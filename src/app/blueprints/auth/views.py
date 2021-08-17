from . import auth
from app.forms import MainForm
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for


@auth.route('/login', methods=['GET','POST'])
def login():

    form = MainForm()

    if form.validate_on_submit():
        return redirect( url_for('home'))

    else:
        return render_template('login.html', form = form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    context = {
        'form': MainForm(),
        'method': request.method
    }

    form = context['form']

    if request.method == 'POST':

        if form.validate_on_submit():

            username = form.username.data
            password = form.password.data
            print(username, password)

            return redirect(url_for('home'))
        
        return render_template('signup.html', **context)

    else:
        return render_template('signup.html', **context)