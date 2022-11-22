from operator import is_
from os import environ

from typing import Optional
import requests
from app import app, connection, cursor, users
from flask import render_template, redirect, url_for, flash, send_file
from app.forms import buildLoginForm, buildSignupForm,medSignupForm,  SignupAccTypeForm,prescriptSignupForm,pharmSignupForm, MedicationSearchForm, PatientSearchForm, SignupAccTypeForm, SelectLoginForm, AppointmentSearchForm, SelectDoctorAppointmentForm, CreateAppointmentForm, AppointmentTypeForm
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
        try: user = users[int(emp_id)]
        except: return None
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SelectLoginForm()
    if form.validate_on_submit():
        if form.account_type.data == 'doctor':
            return redirect(url_for('logindoctor'))
        else:
            return redirect(url_for('loginnurse'))
    return render_template('choose_login.html', form=form, user=None)




@login_required
@app.route('/medication', methods=['GET', 'POST'])
def medication():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = MedicationSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('medication_results', name=form.name.data))
    return render_template('search_medication.html', form=form)



@app.route('/signup/doctor', methods=['GET', 'POST'])
def signup_doctor():
    form = buildSignupForm('doctor')
    if form.validate_on_submit():
        pward = generate_password_hash(form.password.data)
        executeStr = f"INSERT INTO doctor VALUES (%s,%s,%s,%s,%s,%s)"
        dept = form.department.data
        name = form.name.data
        pos = form.position.data
        registered = True
        cursor.execute(executeStr, (int(form.emp_id.data),int(dept), name, pos, registered,pward,))
        connection.commit()
        users[int(form.emp_id.data)]=(form.emp_id.data,pward)
        return redirect(url_for('logindoctor'))
    return render_template('signup_doctor.html', form=form, user=None)

@app.route('/signup/nurse', methods=['GET', 'POST'])
def signup_nurse():
    form = buildSignupForm('nurse')
    if form.validate_on_submit():
        pward = generate_password_hash(form.password.data)
        executeStr = f"INSERT INTO nurse VALUES (%s,%s,%s,%s,%s,%s)"
        dept = form.department.data
        name = form.name.data
        pos = form.position.data
        registered = True
        cursor.execute(executeStr, (int(form.emp_id.data),int(dept), name, pos, registered,pward,))
        connection.commit()
        users[int(form.emp_id.data)]=(form.emp_id.data,pward)
        return redirect(url_for('loginnurse'))
    return render_template('signup_nurse.html', form=form, user=None)


@app.route('/login/doctor', methods=['GET', 'POST'])
def logindoctor():
    form = buildLoginForm('doctor')
    if form.validate_on_submit():
        try: user = User.get(int(form.emp_id.data))
        except: return render_template('login_doctor.html', form=form, user=None, failed=True)
        if user and check_password_hash(user.password,form.password.data):
            login_user(User(user.id,user.password))
            return redirect(url_for('index'))
        else: return render_template('login_doctor.html', form=form, user=None, failed=True)
    return render_template('login_doctor.html', form=form, user=None, failed=False)
    
@app.route('/login/nurse', methods=['GET', 'POST'])
def loginnurse():
    form = buildLoginForm('nurse')
    if form.validate_on_submit():
        try: user = User.get(int(form.emp_id.data))
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


@login_required
@app.route('/myappointments', methods=['GET', 'POST'])
def myappointments():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    return redirect(url_for('doctor_appointments', doctor_id=current_user.id))

@login_required
@app.route('/appointments', methods=['GET', 'POST'])
def search_appointments():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = AppointmentSearchForm()
    cursor.execute(f"select p.first_name, p.last_name, a.admission_date, a.status, d.name from doctor AS d JOIN appointment AS a ON d.doctor_employee_id = a.doctor_employee_id JOIN patient AS p ON a.patient_id = p.patient_id WHERE DATE(a.admission_date) = '{form.date.data}'")
    apps = cursor.fetchall()
    if form.validate_on_submit():
        cursor.execute(f"select p.first_name, p.last_name, a.admission_date, a.status, d.name from doctor AS d JOIN appointment AS a ON d.doctor_employee_id = a.doctor_employee_id JOIN patient AS p ON a.patient_id = p.patient_id WHERE DATE(a.admission_date) = '{form.date.data}'")
        apps = cursor.fetchall()
        print(f"hello {apps}")
        return render_template('search_appointments.html', apps=apps, form=form, user=current_user)
    return render_template('search_appointments.html', apps=apps, form=form, user=current_user)

@login_required
@app.route('/appointments/new/<pat_id>', methods=['GET', 'POST'])
def create_appointment_patient(pat_id):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SelectDoctorAppointmentForm()
    if form.validate_on_submit():
        cursor.execute(f"SELECT * FROM doctor WHERE name LIKE '%{form.doctor_name.data}%'")
        docs = cursor.fetchall()
        return render_template('docs_create_appointment.html', pat_id=pat_id, docs=docs, user=current_user)
    return render_template('pick_doctor_create_appointment.html', form=form, user=current_user)


@login_required
@app.route('/appointments/new/<pat_id>/<doc_id>', methods=['GET', 'POST'])
def create_appointment(pat_id, doc_id):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = AppointmentSearchForm()
    if form.validate_on_submit():
        times = {8:True,9:True,10:True,11:True,12:True,13:True,14:True,15:True,16:True,17:True,18:True}
        cursor.execute(f"select d.name, a.admission_date from appointment AS a JOIN doctor AS d ON d.doctor_employee_id = a.doctor_employee_id where a.doctor_employee_id = 1 and DATE(a.admission_date) = '{form.date.data}'")
        apps = cursor.fetchall()
        cursor.execute(f"SELECT name FROM doctor WHERE doctor_employee_id = {doc_id}")
        doc_name = (cursor.fetchone())[0]
        cursor.execute(f"SELECT first_name, last_name FROM patient WHERE patient_id = {pat_id}")
        pat = cursor.fetchone()
        patient = f"{pat[0]} {pat[1]}"
        for app in apps:
            times[int(app[1].strftime("%H"))]=False
        return render_template('pick_time_create_appointment.html', pat_id=pat_id, patient=patient, doc_name=doc_name, doc_id=doc_id, date=form.date.data, times=times, user=current_user)
    return render_template('search_time_create_appointment.html', form=form, user=current_user)

@login_required
@app.route('/appointments/new/<pat_id>/<doc_id>/<date>/<time>', methods=['GET', 'POST'])
def create_appointment_time(pat_id, doc_id, date, time):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = AppointmentTypeForm()
    if form.validate_on_submit():
        executeStr = f"INSERT INTO appointment(patient_id,doctor_employee_id,nurse_employee_id,status,admission_date,discharge_date,admission_type,exam_type) VALUES (%s,%s, null, 'Not started', %s, null, %s, %s)"
        cursor.execute(executeStr, (pat_id, doc_id,f"{date} {time}",form.admission_type.data,form.exam_type.data,))
        connection.commit()
        return redirect(url_for('myappointments'))
    return render_template('app_type_create_appointment.html', form=form, user=current_user)


# @login_required
# @app.route('/appointments/date/<start_date>/<end_date>', methods=['GET', 'POST'])
# def date_appointments(start_date, end_date):
#     # cursor.execute(f"select * from appointment where admission_date")
#     # results = cursor.fetchall()
#     # cursor.execute(f"select * from doctor where doctor_employee_id = {doctor_id}")
#     # doc = cursor.fetchone()
#     return render_template('doctor_appointments.html', user=current_user)


@login_required
@app.route('/appointments/doc/<doctor_id>', methods=['GET', 'POST'])
def doctor_appointments(doctor_id):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select p.first_name, p.last_name, a.admission_date, a.status from appointment AS a JOIN patient AS p ON a.patient_id = p.patient_id where doctor_employee_id = {doctor_id}")
    results = cursor.fetchall()
    cursor.execute(f"select * from doctor where doctor_employee_id = {doctor_id}")
    doc = cursor.fetchone()
    return render_template('doctor_appointments.html', doc_name=doc[2], appointments=results, user=current_user)


@login_required
@app.route('/patients', methods=['GET', 'POST'])
def patients():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PatientSearchForm()
    if form.validate_on_submit():
        fname = form.first_name.data.replace(" ","")
        lname = form.last_name.data.replace(" ","")
        if fname and lname: return redirect(url_for('patient_result', first_name=fname, last_name=lname))
        if fname: return redirect(url_for('patient_result_fname', first_name=fname))
        if lname: return redirect(url_for('patient_result_lname', last_name=lname))
    return render_template('search_patients.html', form=form, user=current_user)

@login_required
@app.route('/patients/<first_name>/<last_name>', methods=['GET'])
def patient_result(first_name, last_name):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from patient where first_name LIKE '%{first_name}%' and last_name LIKE '%{last_name}%'")
    results = cursor.fetchall()
    return render_template('patients_result.html', name=f"{first_name} {last_name}", results=results, user=current_user)


@login_required
@app.route('/patients/fname/<first_name>', methods=['GET'])
def patient_result_fname(first_name):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from patient where first_name LIKE '%{first_name}%'")
    results = cursor.fetchall()
    return render_template('patients_result.html', name=first_name, results=results, user=current_user)


@login_required
@app.route('/patients/lname/<last_name>', methods=['GET'])
def patient_result_lname(last_name):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from patient where last_name LIKE '%{last_name}%'")
    results = cursor.fetchall()
    return render_template('patients_result.html', name=last_name, results=results, user=current_user)

@app.route('/patient/<id>')
def viewpatient(id):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from patient where patient_id = {id}")
    patient = cursor.fetchone()
    cursor.execute(f"""
                        select m.medication_name, m.generic, m.dosage, p.date_prescribed 
                        from prescription AS p 
                        JOIN medication AS m ON p.medication_id=m.medication_id 
                        where patient_id = {id}
                    """)
    prescriptions = cursor.fetchall()
    cursor.execute(f"""
                        select d.name, a.admission_date, a.status
                        from appointment AS a
                        JOIN doctor AS d
                        ON a.doctor_employee_id = d.doctor_employee_id
                        where a.patient_id = {id}
                        ORDER BY a.admission_date DESC
                    """)
    appointments = cursor.fetchall()
    return render_template('viewpatient.html', patient=patient, prescriptions=prescriptions, appointments=appointments, user=current_user)
    

@login_required
@app.route('/appointments/new/<patient_id>', methods=['GET'])
def new_appointment(patient_id):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from patient where patient_id = {patient_id}")
    patient = cursor.fetchone()
    return render_template('new_appointment.html', patient=patient , user=current_user)


@login_required
@app.route('/medication/<name>', methods=['GET'])
def medication_results(name):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = MedicationSearchForm()    
    cursor.execute(f"select medication_id, medication_name, generic, dosage from medication where medication_id LIKE '%{name}%'")
    results = cursor.fetchall()
    cursor.execute(f"SELECT prescription.medication_id, prescription.patient_id, prescription.pharmacy_ID,prescription.prescription_id,prescription.refills FROM prescription RIGHT JOIN medication ON prescription.medication_id = medication.medication_id where medication_name LIKE'%{name}%'")
    result = cursor.fetchall()
    cursor.execute(f"select pharmacy_id, prescription_id, date_prescribed, patient_id from prescription where patient_id LIKE '%{name}%'")
    result1 = cursor.fetchall()
    cursor.execute(f"SELECT medication_name, generic FROM medication where generic LIKE '%{name}%'")
    result2 = cursor.fetchall()
    cursor.execute(f"select pharmacy_id, name,address from pharmacy where pharmacy_id LIKE'%{name}%'")
    result3 = cursor.fetchall()
    cursor.execute(f"SELECT prescription.patient_id,prescription.medication_id,patient.first_name, prescription.date_prescribed, prescription.pharmacy_ID,patient.last_name FROM prescription LEFT JOIN patient ON prescription.patient_id = patient.patient_id where last_name LIKE'%{name}%'")
    result4 = cursor.fetchall()
    cursor.execute(f"SELECT dosage, medication_name from medication where dosage LIKE'%{name}%'")
    result5 = cursor.fetchall()
    cursor.execute(f"SELECT patient_id, last_name from patient where patient_id LIKE'%{name}%'")
    result6 = cursor.fetchall()
    cursor.execute(f"SELECT * from prescription where prescription_id LIKE'%{name}%'")
    result7 = cursor.fetchall()
    return render_template('medication_results.html',  result=result, result1=result1, result2=result2, result3=result3, result4=result4, result5=result5,result6=result6,result7=result7, name=name, results=results,form=form,user=current_user)

@login_required
@app.route('/medicationadd', methods=['GET', 'POST'])
def medicationADD():
    form = medSignupForm('Medication')
    if form.validate_on_submit():
        executeStr = f"INSERT INTO medication VALUES (%s,%s,%s,%s)"
        Medication_ID = form.emp_id.data
        Medication_name = form.name.data
        Generic = form.department.data
        Dosage = form.position.data
        cursor.execute(executeStr, (int(Medication_ID), Medication_name, Generic, Dosage,))
        connection.commit()
        return redirect(url_for('index'))
    return render_template('medicationadd_result.html', form=form, user=current_user)

@login_required
@app.route('/pharmacyadd', methods=['GET', 'POST'])
def pharmacyADD():
    form = pharmSignupForm('Pharmacy')
    if form.validate_on_submit():
        executeStr = f"INSERT INTO Pharmacy VALUES (%s,%s,%s)"
        Pharmacy_ID = form.emp_id.data
        name = form.name.data
        address = form.department.data
        cursor.execute(executeStr, (int(Pharmacy_ID),name, address,))
        connection.commit()
        return redirect(url_for('index'))
    return render_template('pharmacy_add.html', form=form, user=current_user)

@login_required
@app.route('/prescriptionadd', methods=['GET', 'POST'])
def prescriptionadd():
    form = prescriptSignupForm('prescription')
    if form.validate_on_submit():
        executeStr = f"INSERT INTO prescription VALUES (%s,%s,%s,%s,%s,%s,%s)"
        Prescription_ID = form.emp_id.data
        Pharmacy_ID = form.name.data
        Medication_ID = form.department.data
        Patient_ID = form.position.data
        Date_Prescribed = form.date.data
        Current_diagnosis_severity = form.diagnosis.data
        refills = form.amnt.data
        cursor.execute(executeStr, (int(Prescription_ID),Pharmacy_ID, Medication_ID,Patient_ID,Date_Prescribed, Current_diagnosis_severity,refills,))
        connection.commit()
        return redirect(url_for('index'))
    return render_template('prescriptadd_results.html', form=form, user=current_user)

