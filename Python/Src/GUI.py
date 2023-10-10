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

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def main_Ui():
    global ui,error_msg
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    error_msg = QtWidgets.QLabel(ui.widget)
    if error_msg is not None:
        error_msg.deleteLater()
        error_msg = None
    # username = ui.line_username.text()
    # password = ui.line_password.text()
    ui.createButton.clicked.connect(sign_up_Ui)
    ui.sign_inButton.clicked.connect(homepage_Ui)
    MainWindow.setFixedHeight(1080)
    MainWindow.setFixedWidth(1920)
    MainWindow.showMaximized()

def sign_up_Ui(): 
    global ui
    ui = signup.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.sign_upButton.clicked.connect(main_Ui)

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