import sys
import os
import pandas as pd

def check_user_and_email_signup(df,username_signup, email):
    if (df['Username'] == username_signup).any() and (df['Email'] == email).any():
        return True
    
def check_user_signup(df,username_signup):
    if (df['Username'] == username_signup).any():
        return True
    
def check_email_signup(df, email):
    if (df['Email'] == email).any():
        return True
    
def check_user_and_password_signin(df,username, password):
    if ((df['Username'] == username) & (df['Password'] == password)).any():
        return True