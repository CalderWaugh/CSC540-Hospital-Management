from flask import Flask 

from dotenv import load_dotenv
from os import environ
import mysql.connector
from mysql.connector import Error
# from flask_login import (
#     LoginManager,
#     UserMixin,
#     current_user,
#     login_required,
#     login_user,
#     logout_user,
# )

# force loading of environment variables
load_dotenv('.flaskenv')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MeDClinic'

try:
    connection = mysql.connector.connect(host='localhost',
                                         database=environ.get(''),
                                         user=environ.get(''),
                                         password=environ.get(''))
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        # cursor.execute("select * from test;")
        # record = cursor.fetchone()
        # print(record)

except Error as e:
    print("Error while connecting to MySQL", e)

cursor.execute(f"select * from doctor")
result = cursor.fetchall()
users = {}
for r in result:
    users[r[0]] = (r[0],r[5])

cursor.execute(f"select * from nurse")
result = cursor.fetchall()
for r in result:
    users[r[0]] = (r[0],r[5])

# login_manager = LoginManager(app)


# Add routes
from app import routes