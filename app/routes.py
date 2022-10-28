from operator import is_
from os import environ

from typing import Optional
import requests
from app import app, connection, cursor
from flask import render_template, redirect, url_for, flash, send_file
from app.forms import buildLoginForm, buildSignupForm, SignupAccTypeForm, PatientSearchForm, SignupAccTypeForm, SelectLoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from mysql.connector import Error


from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)

login_manager = LoginManager(app)

# https://github.com/leynier/flask-login-without-orm
# Created the User class and load user function with the help of this github repo
class User(UserMixin):
    def __init__(self, id: str, password: str):
        self.id = id
        self.password = password

    @staticmethod
    def get(emp_id: str) -> Optional["User"]:
        cursor = connection.cursor()
        cursor.execute(f"select * from doctor where doctor_employee_id = {emp_id}")
        result = cursor.fetchone()
        return result

@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    return User.get(user_id)


@app.route('/')
def index():
    print(current_user)
    return render_template('homepage.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SelectLoginForm()
    if form.validate_on_submit():
        if form.account_type.data == 'doctor':
            return redirect(url_for('logindoctor'))
        else:
            return redirect(url_for('loginnurse'))
    return render_template('login.html')

@login_required
@app.route('/patients', methods=['GET', 'POST'])
def patients():
    # if not current_user.is_authenticated:
    #     return redirect(url_for('index'))
    form = PatientSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('patient_result', name=form.name.data))
    return render_template('search_patients.html', form=form)

@app.route('/patients/<name>', methods=['GET'])
def patient_result(name):
    cursor.execute(f"select * from patient where name LIKE '%{name}%'")
    results = cursor.fetchall()
    return render_template('patients_result.html', name=name, results=results)

@app.route('/signup/doctor', methods=['GET', 'POST'])
def signup_doctor():
    form = buildSignupForm('doctor')
    if form.validate_on_submit():
        executeStr = f"INSERT INTO doctor VALUES (%s,%s)"
        cursor.execute(executeStr, (int(form.emp_id.data),form.password.data,))
        connection.commit()
        return redirect(url_for('logindoctor'))
    return render_template('signup_doctor.html', form=form)

@app.route('/login/doctor', methods=['GET', 'POST'])
def logindoctor():
    form = buildLoginForm('doctor')
    if form.validate_on_submit():
        # cursor.execute(f"select * from doctor where doctor_employee_id = {form.emp_id.data}")
        # result = cursor.fetchone()
        user = User.get(form.emp_id.data)
        if user[1] == form.password.data:
            # user["emp_id"] = result[0]
            # user["password"] = result[1]
            login_user(User(user[0],user[1]))
            return redirect(url_for('index'))
    return render_template('login_doctor.html', form=form)
    
@app.route('/login/nurse', methods=['GET', 'POST'])
def loginnurse():
    form = buildLoginForm('nurse')
    return render_template('login_nurse.html', form=form)
    

@app.route('/signup', methods=['GET', 'POST'])
def signupacctype():
    return render_template('signup.html')