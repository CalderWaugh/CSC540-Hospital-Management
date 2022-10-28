from operator import is_
from os import environ

from typing import Optional
import requests
from app import app, connection, cursor, users
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
        user = users[int(emp_id)]
        return User(user[0], user[1])

@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    return User.get(user_id)


@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('homepage.html', user=current_user)
    return render_template('homepage.html', user=None)


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
    return render_template('choose_login.html', form=form, user=current_user)

@login_required
@app.route('/myappointments', methods=['GET', 'POST'])
def myappointments():
    return redirect(url_for('doctor_appointments', doctor_id=current_user))

@login_required
@app.route('/appointments/<doctor_id>', methods=['GET', 'POST'])
def doctor_appointments(doctor_id):
    cursor.execute(f"select * from appointment where doctor_employee_id = {doctor_id}")
    results = cursor.fetchall()
    return render_template('doctor_appointments.html', appointments=results)


@login_required
@app.route('/patients', methods=['GET', 'POST'])
def patients():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PatientSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('patient_result', first_name=form.first_name.data, last_name=form.last_name.data))
    return render_template('search_patients.html', form=form)

@login_required
@app.route('/patients/<first_name>/<last_name>', methods=['GET'])
def patient_result(first_name, last_name):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from patient where first_name LIKE '%{first_name}%' and last_name LIKE '%{last_name}%'")
    results = cursor.fetchall()
    return render_template('patients_result.html', first_name=first_name, last_name=last_name, results=results, user=current_user)

@app.route('/signup/doctor', methods=['GET', 'POST'])
def signup_doctor():
    form = buildSignupForm('doctor')
    if form.validate_on_submit():
        pward = generate_password_hash(form.password.data)
        executeStr = f"INSERT INTO doctor VALUES (%s,%s)"
        cursor.execute(executeStr, (int(form.emp_id.data),pward,))
        connection.commit()
        users[int(form.emp_id.data)]=(form.emp_id.data,pward)
        return redirect(url_for('logindoctor'))
    return render_template('signup_doctor.html', form=form, user=None)

@app.route('/signup/nurse', methods=['GET', 'POST'])
def signup_nurse():
    form = buildSignupForm('nurse')
    if form.validate_on_submit():
        pward = generate_password_hash(form.password.data)
        executeStr = f"INSERT INTO nurse VALUES (%s,%s)"
        cursor.execute(executeStr, (int(form.emp_id.data),pward,))
        connection.commit()
        users[int(form.emp_id.data)]=(form.emp_id.data,pward)
        return redirect(url_for('loginnurse'))
    return render_template('signup_nurse.html', form=form, user=None)

@app.route('/login/doctor', methods=['GET', 'POST'])
def logindoctor():
    form = buildLoginForm('doctor')
    if form.validate_on_submit():
        try: user = User.get(form.emp_id.data)
        except: return render_template('login_doctor.html', form=form, user=None, failed=True)
        if check_password_hash(user.password,form.password.data):
            login_user(User(user.id,user.password))
            return redirect(url_for('index'))
    return render_template('login_doctor.html', form=form, user=None, failed=False)
    
@app.route('/login/nurse', methods=['GET', 'POST'])
def loginnurse():
    form = buildLoginForm('nurse')
    if form.validate_on_submit():
        try: user = User.get(form.emp_id.data)
        except: return render_template('login_nurse.html', form=form, user=None, failed=True)
        if check_password_hash(user.password,form.password.data):
            login_user(User(user.id,user.password))
            return redirect(url_for('index'))
    return render_template('login_nurse.html', form=form, user=None, failed=False)
    
@app.route('/signup', methods=['GET', 'POST'])
def signupacctype():
    form = SignupAccTypeForm()
    if form.validate_on_submit():
        if form.account_type.data == 'doctor':
            return redirect(url_for('signup_doctor'))
        return redirect(url_for('signup_nurse'))
    return render_template('choose_signup.html', form=form, user=None)