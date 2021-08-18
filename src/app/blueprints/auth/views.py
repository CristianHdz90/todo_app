from . import auth
from app.firestore_service import add_user
from app.firestore_service import delete_user
from app.firestore_service import get_user
from app.firestore_service import get_users
from app.forms import MainForm
from app.models import UserData
from app.models import UserModel
from flask import flash
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user


@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    form = MainForm()

    #if the user already is logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':

        if form.validate_on_submit():

            #Bring data from form
            username = form.username.data
            password = form.password.data

            #Create new user in db
            password = {'password': password}
            add_user(username, password)

            return redirect(url_for('home'))
        
        return render_template('signup.html', form=form)

    else:
        return render_template('signup.html', form=form)


@auth.route('/login', methods=['GET','POST'])
def login():

    form = MainForm()

    #if the user already is logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    #If method is 'POST' and went through the validators
    if form.validate_on_submit():
        
        #Data from form
        username_form = form.username.data
        password_form = form.password.data

        print(form.username.data)
        print(form.password.data)

        #Data from db
        user_doc = get_user(username_form)

        #if user exist on db
        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']
            if password_from_db == password_form:

                #Creating the user object
                user_data = UserData(
                    username = username_form,
                    password = password_form
                )
                user = UserModel(user_data)

                #logging in
                login_user(user)

                return redirect( url_for('home'))
            else:
                flash('Wrong password')
        else:
            flash('The user does not exist')
        return render_template('login.html', form = form)
    else:
        return render_template('login.html', form = form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))