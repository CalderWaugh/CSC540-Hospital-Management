from operator import is_
from os import environ

import requests
from app import app
from flask import render_template, redirect, url_for, flash, send_file
from flask_login import login_user, logout_user, login_required
from app.forms import buildLoginForm, SignupEmpForm, SignupStudentForm, SignupAccTypeForm
from werkzeug.security import generate_password_hash, check_password_hash


API_KEY = environ.get('API_KEY')
API_HOST = environ.get('API_HOST')
API_URL = environ.get('API_URL')
EMAIL = environ.get('EMAIL')


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))
    

@app.route('/signup', methods=['GET', 'POST'])
def signupacctype():
    form = SignupAccTypeForm()
    if form.validate_on_submit():
        account_type = form.account_type.data
        if account_type == 'student':
            return redirect(url_for('signupstudent'))
        return redirect(url_for('signupemployer'))
    return render_template('signupacctype.html', form=form, role="loggedout")



# @app.route('/signup/student', methods=['GET', 'POST'])
# def signupstudent():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = SignupStudentForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         if not db.session.query(User).filter_by(username=username).all():
#             user = User(username=username, name=form.name.data, email=form.email.data, account_type='student', phone_number=form.phone_number.data, city=form.city.data, state=form.state.data, role='user')
#             user.set_password(form.password.data)
#             db.session.add(user)
#             db.session.commit()
#             return redirect(url_for('login'))
#     return render_template('signupstudent.html', form=form, role="loggedout")


# @app.route('/signup/employer', methods=['GET', 'POST'])
# def signupemployer():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = SignupEmpForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         if not db.session.query(User).filter_by(username=username).all():
#             user = User(username=username, name=form.name.data, email=form.email.data, account_type='employer', phone_number=form.phone_number.data, company=form.company.data, city=form.city.data, state=form.state.data, role='user')
#             user.set_password(form.password.data)
#             db.session.add(user)
#             db.session.commit()
#             return redirect(url_for('login'))
#     return render_template('signupemployer.html', form=form, role="loggedout")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = buildLoginForm(None)
#     if form.validate_on_submit():
#         user = db.session.query(User).filter_by(username=form.username.data).first()
#         data = {'username': form.username.data}
        
#         if user is None or not user.check_password(form.password.data):
#             print('Login failed', file=sys.stderr)
#             return render_template('login.html', form=form, role="loggedout", failed=True, data=data)

#         print('Ban reason for user', user.username, 'is: ', user.ban_reason)
#         print('Ban boolean:', bool(user.ban_reason))
            
#         if user.ban_reason:
#             print('Banned user', user.username, 'attempted to login')
#             return render_template('banned.html', user=user)
            
#         login_user(user)
#         print('Login successful', file=sys.stderr)
#         return redirect(url_for('index'))
#     return render_template('login.html', form=form, role="loggedout")
