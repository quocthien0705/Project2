import sys
import os
import pandas as pd
import psycopg2 as ps
#Function connect to database
def connect_to_db():
    connectDB = ps.connect(
        host="a-3.postgres.database.azure.com",
        dbname="project",
        user="Project_Health_Care_System",
        password="@healthcare2",
        port=5432
    )
    return connectDB.cursor()
#Function to check username and email when signup account
def check_user_and_email_signup(username_signup, email):
    cursor = connect_to_db()
    cursor.execute(
        """
        SELECT * FROM user_account
        WHERE user_name = %s AND email = %s
        """, 
        (username_signup, email)
    )
    result = cursor.fetchone()
    if result is not None:
        return True
    else:
        return False
#Function to check username when signup account
def check_user_signup(username_signup):
    cursor = connect_to_db()
    cursor.execute(
        """
        SELECT * FROM user_account
        WHERE user_name = %s
        """, 
        (username_signup,)
    )
    result = cursor.fetchone()
    if result is not None:
        return True
    else:
        return False
#Function to check email when signup account
def check_email_signup(email):
    cursor = connect_to_db()
    cursor.execute(
        """
        SELECT * FROM user_account
        WHERE email = %s
        """, 
        (email,)
    )
    result = cursor.fetchone()
    if result is not None:
        return True
    else:
        return False
#Function insert new user when create account
def insert_new_user(username_signup, password_signup, email):
    cursor = connect_to_db()
    cursor.execute(
        """
        INSERT INTO user_account(
            user_name,
            password,
            email
        )
        VALUES (%s,%s,%s)
        """, 
        (username_signup, password_signup, email)
    )
    cursor.connection.commit()
#Function check username and password when login
def check_user_and_password_signin(username, password):
    cursor = connect_to_db()
    cursor.execute(
        """
        SELECT * FROM user_account
        WHERE user_name = %s AND password = %s
        """, 
        (username, password)
    )
    result = cursor.fetchone()
    if result is not None:
        return True
    else:
        return False
#Function to insert new patient profile   
def save_to_db(fullname, dob, sex, height, weight, phone, insur_number, address, note):
    cursor = connect_to_db()
    cursor.execute(
        """
        INSERT INTO profile_of_patient(
            fullname,
            dob,
            sex,
            height,
            weight,
            phone,
            insur_number,
            address,
            note
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, 
        (fullname, dob, sex, height, weight, phone, insur_number, address, note)
    )
    cursor.connection.commit()
#Function to check patient's fullname is exist or not when create patient profile      
def check_fullname_exists(fullname):
    cursor = connect_to_db()
    cursor.execute(
        """
        SELECT * FROM profile_of_patient
        WHERE fullname = %s
        """, 
        (fullname,)
    )
    result = cursor.fetchone()
    if result is not None:
        return True
    else:
        return False

#Function to check table name
def get_tables(fullname):
    cursor = connect_to_db()
    cursor.execute(
        """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        """
    )
    tables = cursor.fetchall()
    cursor.connection.commit()
    # Filter the tables in Python, not SQL
    filtered_tables = [table[0] for table in tables if fullname.replace(" ", "").lower() in table[0].lower()]
    return filtered_tables
