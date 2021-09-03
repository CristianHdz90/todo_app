from . import auth
from app.firestore_service import add_user
from app.firestore_service import delete_user
from app.firestore_service import get_user
from app.forms import DeleteAccountForm
from app.forms import LoginForm
from app.forms import SignupForm
from app.models import UserData
from app.models import UserModel
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


@auth.route('signup/', methods=['GET', 'POST'])
def signup():

    form = SignupForm()

    #if the user already is logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        #Data from the form
        username_form = form.username.data
        password_form = form.password.data

        #Data from db
        user_doc = get_user(username_form)

        #if the user doesn't exist
        if user_doc.to_dict() is None:

            #Hashing password
            password_hash =  generate_password_hash(password_form)

            #Create new user in db
            add_user(username_form, password_hash)

            #Creating the user object
            user_data = UserData(
                username = username_form,
                password = password_hash
            )
            user = UserModel(user_data)

            #logging in
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('The user already exist, try other username')
    return render_template('signup.html', form=form)


@auth.route('login/', methods=['GET','POST'])
def login():

    form = LoginForm()

    #if the user already is logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        #Data from form
        username_form = form.username.data
        password_form = form.password.data

        #Data from db
        user_doc = get_user(username_form)

        #if user exist on db
        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']

            #if the password is right
            if check_password_hash(password_from_db, password_form):

                #Creating the user object
                user_data = UserData(
                    username = username_form,
                    password = password_from_db
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


@auth.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('delete-account', methods=['POST'])
@login_required
def delete_account():
    delete_account_form = DeleteAccountForm()
    user_id = current_user.id
    if delete_account_form.validate_on_submit():
        logout_user()
        delete_user(user_id)
        return redirect(url_for('auth.signup'))
    else:
        errors = delete_account_form.description.errors
        for error in errors:
            flash(error)
        return redirect(url_for('home'))