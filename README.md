# CSC540-Hospital-Management
Hospital Management Software Project for CSC 540 at SCSU

# Testing
```
Doctor- id: 1234 password: Rjenkins
Nurse- id: 1101 password: Jbean
```

# (First time running) How to run
```
Go to base project folder then do the following commands in order:
--------------------------------------------------------------
Step # | Command / Step
--------------------------------------------------------------
Step 1 | Run the DDL in the populate_db.sql file
Step 2 | Enter your mysql password in the .flaskenv file
Step 3 | python -m venv venv
Step 4 | .\venv\Scripts\activate
Step 5 | python -m pip install -r requirements.txt
Step 6 | python -m flask run
--------------------------------------------------------------
Explanation
--------------------------------------------------------------
Step 1 - Create and populate the database
Step 2 - Enable connection to the database
Step 3 - Create a virtual environment to run the application
Step 4 - Activate the virtual environment
Step 5 - Install the required packages to run the application
Step 6 - Run the application
--------------------------------------------------------------
```

# (After first time) How to run
```
--------------------------------------------------------------
Step   | Command
--------------------------------------------------------------
Step 1 | .\venv\Scripts\activate
Step 2 | python -m flask run
--------------------------------------------------------------
--------------------------------------------------------------
Explanation
--------------------------------------------------------------
Since you already created the virtual environment and
installed the required packages in the virtual environment
all you have to do following the first time running, is
activate the virtual environment, and run the application.
--------------------------------------------------------------
```

