from flask_wtf import FlaskForm
from wtforms.fields import PasswordField
from wtforms.fields import StringField
from wtforms.fields import SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask import session


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')


class TodoForm(FlaskForm):
    description = StringField('Description', 
        validators=[DataRequired()],
        render_kw={"placeholder":"write something..."}
    )
    submit = SubmitField('Create')


class UpdateTodoForm(FlaskForm):
    description = StringField('Description',
        validators=[DataRequired()],
        render_kw={"placeholder":"something else"}
    )
    submit = SubmitField('Update')


def delete_account_content_field(form, field):
    username = session['_user_id'].upper()
    username_form = field.data
    if username_form != username:
        raise ValidationError(f'You must type "{username}" instead of "{username_form}"')


class DeleteAccountForm(FlaskForm):
    description = StringField(
        validators=[
            DataRequired(message='You cannot send the field empty'),
            delete_account_content_field
        ]
    )
    submit = SubmitField('Delete account')