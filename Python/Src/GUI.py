import img_src_rc
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import os
import pandas as pd
import login
import signup
import homepage
######################################################################
ROOT_PATH      = os.path.dirname(os.path.abspath(__file__))
DATA_PATH      = os.path.join(ROOT_PATH,'..','Data')
font = QtGui.QFont()
font.setFamily("Rockwell")
error_msg = None
signup_error_msg = None

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def sign_up_Ui(): 
    global ui,username_signup,password_signup,confirm,email,signup_error_msg
    ui = signup.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.sign_upButton.clicked.connect(on_sign_up_clicked)
    MainWindow.setFixedHeight(1080)
    MainWindow.setFixedWidth(1920)
    MainWindow.showMaximized()  
    signup_error_msg = QtWidgets.QLabel(ui.widget)
    if signup_error_msg is not None:
        signup_error_msg.deleteLater()
        signup_error_msg = None
def on_sign_up_clicked():
    global username_signup, password_signup, confirm, email, signup_error_msg
    username_signup = ui.line_username_signup.text()
    password_signup = ui.line_password_signup.text()
    confirm = ui.line_confirm.text()
    email = ui.line_email.text()

    
    if signup_error_msg is None:
        signup_error_msg = QtWidgets.QLabel(ui.widget)
        signup_error_msg.setStyleSheet("background-color: rgba(0,0,0,0);color: red")
        font.setPointSize(10)
        signup_error_msg.setFont(font)

   
    if len(username_signup) == 0 or len(password_signup) == 0 or len(confirm) == 0 or len(email) == 0:
        signup_error_msg.setText("Please input all fields.")
        signup_error_msg.move(80, 340)
        signup_error_msg.show()
    else:
        df = pd.read_csv(os.path.join(DATA_PATH,'Login_Account.csv'))

        
        if (df['Username'] == username_signup).any() and (df['Email'] == email).any():
            signup_error_msg.setText("Username and Email already exist.")
            signup_error_msg.setGeometry(QtCore.QRect(70, 340, 300, 30))
            signup_error_msg.show()
        
        elif (df['Username'] == username_signup).any():
            signup_error_msg.setText("Username already exists.")
            signup_error_msg.setGeometry(QtCore.QRect(70, 340, 300, 30))
            signup_error_msg.show()
        
        elif (df['Email'] == email).any():
            signup_error_msg.setText("Email already exists.")
            signup_error_msg.setGeometry(QtCore.QRect(70, 340, 300, 30))
            signup_error_msg.show()
        
        elif '@' not in email:
            signup_error_msg.setText("Please enter a valid email.")
            signup_error_msg.setGeometry(QtCore.QRect(70, 340, 300, 30))
            signup_error_msg.show()
        
        elif password_signup != confirm:
            signup_error_msg.setText("Confirm Password does not match.")
            signup_error_msg.setGeometry(QtCore.QRect(70, 340, 300, 30))
            signup_error_msg.show()
        else:
            print(username_signup,password_signup,confirm,email)  
            data = pd.DataFrame([[username_signup, password_signup, email]], columns=['Username', 'Password', 'Email'])
            data.to_csv(os.path.join(DATA_PATH,'Login_Account.csv'), mode='a', header=False, index=False)
            
            main_Ui()
    
def main_Ui():
    global ui,error_msg
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)

    error_msg = QtWidgets.QLabel(ui.widget)
    if error_msg is not None:
        error_msg.deleteLater()
        error_msg = None

    ui.createButton.clicked.connect(sign_up_Ui)
    
    ui.sign_inButton.clicked.connect(homepage_Ui)
    MainWindow.setFixedHeight(1080)
    MainWindow.setFixedWidth(1920)
    MainWindow.showMaximized()

def homepage_Ui():
    global ui,error_msg
    username = ui.line_username.text()
    password = ui.line_password.text()

    if error_msg is None:
        error_msg = QtWidgets.QLabel(ui.widget)
        error_msg.setStyleSheet("background-color: rgba(0,0,0,0);color: red")
        font.setPointSize(10)
        error_msg.setFont(font)
        
    if len(username)==0 or len(password)==0:
        
        error_msg.setText("Please input all fields.")
        error_msg.move(80, 270)
        error_msg.show()
        
    else:
        df = pd.read_csv(os.path.join(DATA_PATH,'Login_Account.csv'))
        if ((df['Username'] == username) & (df['Password'] == password)).any():
            print(username,password)
            ui = homepage.Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.setFixedHeight(1080)
            MainWindow.setFixedWidth(1920)
            MainWindow.showMaximized()
        else:
            error_msg.setText("Invalid username or password.")
            error_msg.setGeometry(QtCore.QRect(70, 265, 300, 30))
            error_msg.show()
    
    
main_Ui()
sys.exit(app.exec_())