import img_src_rc
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
import os
import pandas as pd
import stacked
import login
import signup
from get_taskbar_height import get_taskbar_height
import sidebar
ROOT_PATH      = os.path.dirname(os.path.abspath(__file__))
DATA_PATH      = os.path.join(ROOT_PATH,'..','Data')
font = QtGui.QFont()
font.setFamily("Rockwell")
error_msg = None
signup_error_msg = None
ui = None
taskbar_height = get_taskbar_height()
app = QtWidgets.QApplication(sys.argv)
Mainwindow = QtWidgets.QMainWindow()

def login_Ui():
    global ui,error_msg
    ui = stacked.Ui_MainWindow()
    ui.setupUi(Mainwindow)
    ui.stackedWidget.setCurrentIndex(0)
    error_msg = QtWidgets.QLabel(ui.widget_login)
    if error_msg is not None:
        error_msg.deleteLater()
        error_msg = None    
    ui.sign_inButton_2.clicked.connect(homepage_Ui)
    ui.createButton_2.clicked.connect(lambda:signup_Ui(ui))
    Mainwindow.setFixedHeight(1080-taskbar_height)
    Mainwindow.setFixedWidth(1920)
    Mainwindow.showMaximized()
def signup_Ui(ui):
    global signup_error_msg
    # ui = stacked.Ui_MainWindow()
    # ui.setupUi(Mainwindow)
    ui.stackedWidget.setCurrentIndex(1)
    ui.sign_upButton_2.clicked.connect(lambda:on_sign_up_clicked(ui))
    signup_error_msg = QtWidgets.QLabel(ui.widget_signup)
    if signup_error_msg is not None:
        signup_error_msg.deleteLater()
        signup_error_msg = None    
    Mainwindow.setFixedHeight(1080-taskbar_height)
    Mainwindow.setFixedWidth(1920)
    Mainwindow.showMaximized()
def on_sign_up_clicked(ui):
    global username_signup, password_signup, confirm, email, signup_error_msg
    # ui = stacked.Ui_MainWindow()
    # ui.setupUi(Mainwindow)
    # ui.stackedWidget.setCurrentIndex(1)    
    username_signup = ui.line_username_signup_2.text()
    password_signup = ui.line_password_signup_2.text()
    confirm = ui.line_confirm_2.text()
    email = ui.line_email_2.text()

    
    if signup_error_msg is None:
        signup_error_msg = QtWidgets.QLabel(ui.widget_signup)
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
            signup_error_msg.setGeometry(QtCore.QRect(55, 345, 300, 30))
            signup_error_msg.show()
        
        elif (df['Username'] == username_signup).any():
            signup_error_msg.setText("Username already exists.")
            signup_error_msg.setGeometry(QtCore.QRect(70, 345, 300, 30))
            signup_error_msg.show()
        
        elif (df['Email'] == email).any():
            signup_error_msg.setText("Email already exists.")
            signup_error_msg.setGeometry(QtCore.QRect(70, 345, 300, 30))
            signup_error_msg.show()
        
        elif '@' not in email:
            signup_error_msg.setText("Please enter a valid email.")
            signup_error_msg.setGeometry(QtCore.QRect(70, 345, 300, 30))
            signup_error_msg.show()
        elif len(password_signup)<8:
            signup_error_msg.setText("Passwords must be at least 8 characters")
            signup_error_msg.setGeometry(QtCore.QRect(42, 345, 300, 30))
            signup_error_msg.show()            
        elif password_signup != confirm:
            signup_error_msg.setText("Confirm Password does not match.")
            signup_error_msg.setGeometry(QtCore.QRect(60, 345, 300, 30))
            signup_error_msg.show()
        else:
            print(username_signup,password_signup,confirm,email)  
            data = pd.DataFrame([[username_signup, password_signup, email]], columns=['Username', 'Password', 'Email'])
            data.to_csv(os.path.join(DATA_PATH,'Login_Account.csv'), mode='a', header=False, index=False)
            
            login_Ui()
def create_main_window():
    Mainwindow = QMainWindow()
    ui = sidebar.Ui_MainWindow()
    ui.setupUi(Mainwindow)

    ui.icon_only_widget.hide()
    ui.stackedWidget.setCurrentIndex(1)
    ui.home_btn_2.setChecked(True)
    # Connect signals to slots
    ui.stackedWidget.currentChanged.connect(lambda: on_stackedWidget_currentChanged(ui, ui.stackedWidget.currentIndex()))
    ui.home_btn_1.toggled.connect(lambda: on_home_btn_toggled(ui))
    ui.home_btn_2.toggled.connect(lambda: on_home_btn_toggled(ui))
    ui.display_btn_1.toggled.connect(lambda: on_display_btn_toggled(ui))
    ui.display_btn_2.toggled.connect(lambda: on_display_btn_toggled(ui))
    ui.newprofile_btn_1.toggled.connect(lambda: on_newprofile_btn_toggled(ui))
    ui.newprofile_btn_2.toggled.connect(lambda: on_newprofile_btn_toggled(ui))
    ui.uart_btn_1.toggled.connect(lambda: on_uart_btn_toggled(ui))
    ui.uart_btn_2.toggled.connect(lambda: on_uart_btn_toggled(ui))

    return Mainwindow

def on_stackedWidget_currentChanged(ui, index):
    btn_list = ui.icon_only_widget.findChildren(QPushButton) \
                + ui.full_menu_widget.findChildren(QPushButton)
    
    for btn in btn_list:
        if index in [5, 6]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
        else:
            btn.setAutoExclusive(True)

def on_home_btn_toggled(ui):
    ui.stackedWidget.setCurrentIndex(1)

def on_display_btn_toggled(ui):
    ui.stackedWidget.setCurrentIndex(3)

def on_newprofile_btn_toggled(ui):
    ui.stackedWidget.setCurrentIndex(2)

def on_uart_btn_toggled(ui):
    ui.stackedWidget.setCurrentIndex(4)
def homepage_Ui():
    global ui,error_msg,username,password
    username = ui.line_username_2.text()
    password = ui.linepassword_2.text()

    if error_msg is None:
        error_msg = QtWidgets.QLabel(ui.widget_login)
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
            # print(username,password)
            ui = sidebar.Ui_MainWindow()
            ui.setupUi(Mainwindow)
            Mainwindow.setFixedHeight(1080-taskbar_height-35)
            Mainwindow.setFixedWidth(1920)  
            Mainwindow.showMaximized()
            ui.icon_only_widget.hide()
            ui.stackedWidget.setCurrentIndex(1)
            ui.home_btn_2.setChecked(True)
            # Connect signals to slots
            ui.stackedWidget.currentChanged.connect(lambda: on_stackedWidget_currentChanged(ui, ui.stackedWidget.currentIndex()))
            ui.home_btn_1.toggled.connect(lambda: on_home_btn_toggled(ui))
            ui.home_btn_2.toggled.connect(lambda: on_home_btn_toggled(ui))
            ui.display_btn_1.toggled.connect(lambda: on_display_btn_toggled(ui))
            ui.display_btn_2.toggled.connect(lambda: on_display_btn_toggled(ui))
            ui.newprofile_btn_1.toggled.connect(lambda: on_newprofile_btn_toggled(ui))
            ui.newprofile_btn_2.toggled.connect(lambda: on_newprofile_btn_toggled(ui))
            ui.uart_btn_1.toggled.connect(lambda: on_uart_btn_toggled(ui))
            ui.uart_btn_2.toggled.connect(lambda: on_uart_btn_toggled(ui))
        else:
            error_msg.setText("Invalid username or password.")
            error_msg.setGeometry(QtCore.QRect(70, 265, 300, 30))
            error_msg.show()
login_Ui()

sys.exit(app.exec_())