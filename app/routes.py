from datetime import date, datetime
from operator import is_
from os import environ

from typing import Optional
import requests
from app import app, connection, cursor, users
from flask import render_template, redirect, url_for, flash, send_file
from app.forms import buildLoginForm, buildSignupForm,MedicationForm,  SignupAccTypeForm,AddPrescriptionForm,pharmSignupForm, MedicationSearchForm, PatientSearchForm, SignupAccTypeForm, SelectLoginForm, AppointmentSearchForm, SelectDoctorAppointmentForm, CreateAppointmentForm, AppointmentTypeForm, BuildEditAppointmentForm
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

session = {'url':''}

# Set page results for the application
results = 10
pages = []

# https://github.com/leynier/flask-login-without-orm
# Created the User class and load user function with the help of this github repo
class User(UserMixin):
    def __init__(self, id: str, password: str, doc: bool):
        self.id = id
        self.password = password
        self.doc = doc

    @staticmethod
    def get(emp_id: str) -> Optional["User"]:
        try: user = users[int(emp_id)]
        except: return None
        return User(user[0], user[1], user[2])

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
        users[int(form.emp_id.data)]=(form.emp_id.data,pward,True)
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
        users[int(form.emp_id.data)]=(form.emp_id.data,pward,False)
        return redirect(url_for('loginnurse'))
    return render_template('signup_nurse.html', form=form, user=None)


@app.route('/login/doctor', methods=['GET', 'POST'])
def logindoctor():
    form = buildLoginForm('doctor')
    if form.validate_on_submit():
        try: user = User.get(int(form.emp_id.data))
        except: return render_template('login_doctor.html', form=form, user=None, failed=True)
        if user and check_password_hash(user.password, form.password.data):
            login_user(User(user.id,user.password,True))
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
            login_user(User(user.id,user.password,False))
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

###########################################################################################################
#############################       APPOINTMENTS SECTION        ###########################################
###########################################################################################################

@login_required
@app.route('/myappointments', methods=['GET', 'POST'])
def myappointments():
    if not current_user.is_authenticated or not current_user.doc:
        return redirect(url_for('index'))
    cursor.execute(f"select name from doctor where doctor_employee_id = {current_user.id}")
    doc = (cursor.fetchone())[0]
    return redirect(url_for('docdate_appointments', name=doc, date=date.today(), page=1))

@login_required
@app.route('/appointments', methods=['GET', 'POST'])
def search_appointments():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = AppointmentSearchForm()
    if form.validate_on_submit():
        doc_name = form.doc_name.data
        date = form.date.data
        if doc_name:
            return redirect(url_for('docdate_appointments', name=doc_name, date=date, page=1))
        return redirect(url_for('date_appointments', date=date, page=1))
    return render_template('search_appointments.html',form=form, user=current_user)

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
@app.route('/appointments/date/<date>/<page>', methods=['GET', 'POST'])
def date_appointments(date, page):
    cursor.execute(f"""
                        select p.first_name, p.last_name, DATE_FORMAT(a.admission_date,'%h:%i %p'), a.status, d.name, a.discharge_date, p.patient_id, a.admission_date
                        from doctor AS d 
                        JOIN appointment AS a ON d.doctor_employee_id = a.doctor_employee_id 
                        JOIN patient AS p ON a.patient_id = p.patient_id 
                        WHERE DATE(a.admission_date) = '{date}'
                        ORDER BY a.admission_date ASC
                    """)
    apps = cursor.fetchall()
    pages = []
    y=1
    for x in range(0,len(apps),results):
        pages.append(y)
        y+=1
    session['url'] = url_for('date_appointments', date=date, page=page)
    page = int(page)-1
    apps = apps[page*results:(page*results)+results]
    return render_template('appointment_date.html', date=date, page=page+1,pages=pages, apps=apps, user=current_user)

@login_required
@app.route('/appointments/docdate/<name>/<date>/<page>', methods=['GET', 'POST'])
def docdate_appointments(name, date, page):
    cursor.execute(f"""
                        select p.first_name, p.last_name, DATE_FORMAT(a.admission_date,'%h:%i %p'), a.status, d.name, a.discharge_date, p.patient_id, d.name, a.admission_date
                        from doctor AS d 
                        JOIN appointment AS a ON d.doctor_employee_id = a.doctor_employee_id 
                        JOIN patient AS p ON a.patient_id = p.patient_id 
                        WHERE DATE(a.admission_date) = '{date}' and d.name LIKE '%{name}%'
                        ORDER BY a.admission_date ASC
                    """)
    apps = cursor.fetchall()
    pages = []
    y=1
    for x in range(0,len(apps),results):
        pages.append(y)
        y+=1
    session['url'] = url_for('docdate_appointments', name=name, date=date, page=page)
    page = int(page)-1
    apps = apps[page*results:(page*results)+results]
    return render_template('appointment_docdate.html', doc_name=name, date=date, name=name, page=page+1,pages=pages, apps=apps, user=current_user)

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
        cursor.execute(f"select d.name, a.admission_date from appointment AS a JOIN doctor AS d ON d.doctor_employee_id = a.doctor_employee_id where a.doctor_employee_id = {doc_id} and DATE(a.admission_date) = '{form.date.data}'")
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
        return redirect(url_for('search_appointments'))
    return render_template('app_type_create_appointment.html', form=form, user=current_user)

@login_required
@app.route('/appointments/edit/<doc_name>/<admin_date>', methods=['GET', 'POST'])
def edit_appointment(doc_name, admin_date):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    print(admin_date)
    cursor.execute(f"""
                        SELECT a.status 
                        FROM appointment AS a 
                        JOIN doctor AS d ON a.doctor_employee_id = d.doctor_employee_id
                        WHERE a.admission_date = '{admin_date}' and d.name = '{doc_name}'
                    """)
    stat = (cursor.fetchone())[0]
    form = BuildEditAppointmentForm(stat)
    if form.validate_on_submit():
        print(doc_name)
        cursor.execute(f"select doctor_employee_id from doctor where name = '{doc_name}'")
        doc_id = (cursor.fetchone())[0]
        if form.status.data != 'completed':
            cursor.execute(f"""
                UPDATE appointment 
                SET status = '{form.status.data}', discharge_date = null
                WHERE doctor_employee_id = {doc_id} and admission_date = '{admin_date}'
                            """)
        else:
            cursor.execute(f"""
                UPDATE appointment 
                SET status = 'completed', discharge_date = '{datetime.now()}'
                WHERE doctor_employee_id = {doc_id} and admission_date = '{admin_date}'
                            """)
        connection.commit()
        return redirect(session['url'])
    return render_template('edit_appointment.html', form=form, user=current_user)


###########################################################################################################
#############################         PATIENTS SECTION          ###########################################
###########################################################################################################

@login_required
@app.route('/patients', methods=['GET', 'POST'])
def patients():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PatientSearchForm()
    if form.validate_on_submit():
        fname = form.first_name.data.replace(" ","")
        lname = form.last_name.data.replace(" ","")
        if fname and lname: return redirect(url_for('patient_result', first_name=fname, last_name=lname, page=1))
        if fname: return redirect(url_for('patient_result_fname', first_name=fname, page=1))
        if lname: return redirect(url_for('patient_result_lname', last_name=lname, page=1))
    return render_template('search_patients.html', form=form, user=current_user)

@login_required
@app.route('/patients/<first_name>/<last_name>/<page>', methods=['GET'])
def patient_result(first_name, last_name, page):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from patient where first_name LIKE '%{first_name}%' and last_name LIKE '%{last_name}%'")
    pats = cursor.fetchall()
    route = "fl"
    pages = []
    y=1
    for x in range(0,len(pats),results):
        pages.append(y)
        y+=1
    page = int(page)-1
    pats = pats[page*results:(page*results)+results]
    return render_template('patients_result.html', page = page+1, pages=pages, route=route, name=f"{first_name} {last_name}", results=pats, user=current_user)


@login_required
@app.route('/patients/fname/<first_name>/<page>', methods=['GET'])
def patient_result_fname(first_name, page):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from patient where first_name LIKE '%{first_name}%' ORDER BY last_name, first_name DESC ")
    pats = cursor.fetchall()
    route = "f"
    pages = []
    y=1
    for x in range(0,len(pats),results):
        pages.append(y)
        y+=1
    page = int(page)-1
    pats = pats[page*results:(page*results)+results]
    return render_template('patients_result.html', page = page+1, pages=pages, route=route, name=first_name, results=pats, user=current_user)


@login_required
@app.route('/patients/lname/<last_name>/<page>', methods=['GET'])
def patient_result_lname(last_name, page):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from patient where last_name LIKE '%{last_name}%'")
    pats = cursor.fetchall()
    route = "l"
    pages = []
    y=1
    for x in range(0,len(pats),results):
        pages.append(y)
        y+=1
    page = int(page)-1
    pats = pats[page*results:(page*results)+results]
    return render_template('patients_result.html', page = page+1, pages=pages, route=route, name=last_name, results=pats, user=current_user)

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
                        select d.name, DATE_FORMAT(a.admission_date,'%M %d, %Y %h:%i %p'), a.status
                        from appointment AS a
                        JOIN doctor AS d
                        ON a.doctor_employee_id = d.doctor_employee_id
                        where a.patient_id = {id}
                        ORDER BY a.admission_date DESC
                    """)
    appointments = cursor.fetchall()
    return render_template('viewpatient.html', patient=patient, prescriptions=prescriptions, appointments=appointments, user=current_user)

###########################################################################################################
#############################        MEDICATION SECTION         ###########################################
###########################################################################################################

@login_required
@app.route('/medication', methods=['GET', 'POST'])
def medication():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = MedicationSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('medication_results', name=form.name.data))
    return render_template('search_medication.html', form=form)

@login_required
@app.route('/medications', methods=['GET', 'POST'])
def medications():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = MedicationSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('medication_results', name=form.name.data, page=1))
    return render_template('search_medication.html', form=form, user=current_user)

@login_required
@app.route('/medications/<name>/<page>', methods=['GET'])
def medication_results(name,page):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"select * from medication where LOWER(medication_name) LIKE '%{name}%'")
    meds = cursor.fetchall()
    pages = []
    y=1
    for x in range(0,len(meds),results):
        pages.append(y)
        y+=1
    page = int(page)-1
    meds = meds[page*results:(page*results)+results]
    return render_template('medication_results.html', page=(page+1), pages=pages, med_name=name, meds=meds, user=current_user)

@login_required
@app.route('/medicationadd', methods=['GET', 'POST'])
def medicationADD():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = MedicationForm()
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

###########################################################################################################
#############################         PHARMACY SECTION          ###########################################
###########################################################################################################

@login_required
@app.route('/pharmacyadd', methods=['GET', 'POST'])
def pharmacyADD():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
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

###########################################################################################################
#############################       PRESCRIPTIONS SECTION       ###########################################
###########################################################################################################

@login_required
@app.route('/prescriptions/<med_id>/<page>', methods=['GET', 'POST'])
def prescriptions_medication(med_id,page):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    cursor.execute(f"""
                    select pa.first_name, pa.last_name, m.dosage, pr.date_prescribed, pr.refills, ph.name, m.medication_name
                    from medication AS m 
                    JOIN prescription AS pr ON m.medication_id = pr.medication_id
                    JOIN pharmacy AS ph ON pr.pharmacy_id = ph.pharmacy_id
                    JOIN patient AS pa ON pr.patient_id = pa.patient_id
                    where m.medication_id = {med_id}
                    """)
    prescriptions = cursor.fetchall()
    
    pages = []
    y=1
    for x in range(0,len(prescriptions),results):
        pages.append(y)
        y+=1
    page = int(page)-1
    prescriptions = prescriptions[page*results:(page*results)+results]
    if prescriptions: med_name = prescriptions[0][6]
    else: med_name = ''
    return render_template('prescriptions_medication.html', pages=pages, page=page+1, med_name=med_name, med_id=med_id, prescriptions=prescriptions, user=current_user)

@login_required
@app.route('/prescription/add/<pat_id>', methods=['GET', 'POST'])
def prescriptionadd(pat_id):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = AddPrescriptionForm()
    if form.validate_on_submit():
        executeStr = f"INSERT INTO prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) VALUES (%s,%s,%s,%s,%s,%s)"
        Pharmacy_ID = form.pharmacy_id.data
        Medication_ID = form.medication_id.data
        Date_Prescribed = date.today()
        Current_diagnosis_severity = form.diagnosis.data
        refills = form.refills.data
        cursor.execute(executeStr, (Pharmacy_ID, Medication_ID,pat_id,Date_Prescribed, Current_diagnosis_severity,refills,))
        connection.commit()
        return redirect(url_for('index'))
    return render_template('prescriptadd_results.html', form=form, user=current_user)

