from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class MainForm(FlaskForm):
    username = StringField('Username', validators=[ DataRequired(), Length(min= 5, max=20)])
    password = PasswordField('Password', validators=[ DataRequired(), Length(min= 8, max=20)])
    submit = SubmitField('Send')