from flask import Flask 

from dotenv import load_dotenv
from os import environ
import mysql.connector
from mysql.connector import Error

# force loading of environment variables
load_dotenv('.flaskenv')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MeDClinic'

try:
    connection = mysql.connector.connect(host=environ.get('MYSQL_IP'),
                                         database=environ.get('MYSQL_DB'),
                                         user=environ.get('MYSQL_USER'),
                                         password=environ.get('MYSQL_PASS'))
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

except Error as e:
    print("Error while connecting to MySQL", e)

cursor.execute(f"select * from doctor")
result = cursor.fetchall()
users = {}
for r in result:
    users[r[0]] = (r[0],r[5], True)

cursor.execute(f"select * from nurse")
result = cursor.fetchall()
for r in result:
    users[r[0]] = (r[0],r[5], False)

# Add routes
from app import routes