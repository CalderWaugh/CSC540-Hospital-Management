from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, StringField, PasswordField, SelectField, ValidationError, BooleanField, DateField
from wtforms.validators import DataRequired, Optional

def buildLoginForm(data):
    if data:
        class LoginForm(FlaskForm):
            username = StringField('Username', validators=[DataRequired()], default=data['username'])
            password = PasswordField('Password', validators=[DataRequired()])
            submit = SubmitField('Log in')
    else:
        class LoginForm(FlaskForm):
            username = StringField('Username', validators=[DataRequired()])
            password = PasswordField('Password', validators=[DataRequired()])
            submit = SubmitField('Log in')
    return LoginForm()

class SignupEmpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    phone_number = StringField('Phone', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')

class SignupStudentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    phone_number = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')

class SignupAccTypeForm(FlaskForm):
    account_type = SelectField('Account Type', choices=['student', 'employer'], validators=[DataRequired()])
    submit = SubmitField('Continue')

class UserSearchForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Search')