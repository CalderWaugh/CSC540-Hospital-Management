from flask import Flask 

from dotenv import load_dotenv
from os import environ

# force loading of environment variables
load_dotenv('.flaskenv')

# Get the environment variables from .flaskenv
IP = environ.get('MYSQL_IP')
USERNAME = environ.get('MYSQL_USER')
PASSWORD = environ.get('MYSQL_PASS')
DB_NAME = environ.get('MYSQL_DB')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MeDClinic'

# Specify the connection parameters/credentials for the database
DB_CONFIG_STR = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{IP}/{DB_NAME}"

# Add routes
from app import routes