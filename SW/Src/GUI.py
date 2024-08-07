import img_src_rc
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QVBoxLayout,QMessageBox
import sys
from pyqtgraph import PlotWidget, mkPen,AxisItem
import pandas as pd
import stacked
import open_web
import threading
# from get_taskbar_height import get_taskbar_height
import sidebar
from azure_communication_function import *
from support_function import *
font = QtGui.QFont()
font.setFamily("Rockwell")
error_msg = None
current_user = None
table_name = None
signup_error_msg = None
error_profile = None
ui = None
# taskbar_height = get_taskbar_height()
app = QtWidgets.QApplication(sys.argv)
Mainwindow = QtWidgets.QMainWindow()
manager = IdentityManager(connection_string)
def login_Ui():
    global ui,error_msg
    write_path_to_json()
    ui = stacked.Ui_MainWindow()
    ui.setupUi(Mainwindow)
    ui.stackedWidget.setCurrentIndex(0)
    error_msg = QtWidgets.QLabel(ui.widget_login)
    if error_msg is not None:
        error_msg.deleteLater()
        error_msg = None    
    ui.sign_inButton_2.clicked.connect(homepage_Ui)
    ui.createButton_2.clicked.connect(lambda:signup_Ui(ui))
    # Mainwindow.setFixedHeight(994)
    # Mainwindow.setFixedWidth(1920)
    # Mainwindow.resize(1000,600)
    Mainwindow.showMaximized()
def signup_Ui(ui):
    global signup_error_msg
    # ui = stacked.Ui_MainWindow()
    # ui.setupUi(Mainwindow)
    ui.stackedWidget.setCurrentIndex(1)
    ui.back_Button.clicked.connect(login_Ui)
    ui.sign_upButton_2.clicked.connect(lambda:on_sign_up_clicked(ui))
    signup_error_msg = QtWidgets.QLabel(ui.widget_signup)
    if signup_error_msg is not None:
        signup_error_msg.deleteLater()
        signup_error_msg = None    
    # Mainwindow.setFixedHeight(994)
    # Mainwindow.setFixedWidth(1920)
    # Mainwindow.resize(1000,600)
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
    
    id_value = manager.create_and_add_user_to_db(cursor, username_signup)
    cursor.execute(f"ALTER TABLE doctor_threadmanage ADD COLUMN {username_signup} text")
    cursor.connection.commit()


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
        # df = pd.read_csv(os.path.join(DATA_PATH,'Login_Account.csv'))

        
        if check_user_and_email_signup(username_signup,email):
            signup_error_msg.setText("Username and Email already exist.")
            signup_error_msg.setGeometry(QtCore.QRect(55, 345, 300, 30))
            signup_error_msg.show()
        
        elif check_user_signup(username_signup):
            signup_error_msg.setText("Username already exists.")
            signup_error_msg.setGeometry(QtCore.QRect(70, 345, 300, 30))
            signup_error_msg.show()
        
        elif check_email_signup(email):
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
            # print(username_signup,password_signup,confirm,email)  
            # data = pd.DataFrame([[username_signup, password_signup, email]], columns=['Username', 'Password', 'Email'])
            # data.to_csv(os.path.join(DATA_PATH,'Login_Account.csv'), mode='a', header=False, index=False)
            insert_new_user(username_signup, password_signup, email, id_value)
            login_Ui()

def on_stackedWidget_currentChanged(ui, index):
    btn_list = ui.icon_only_widget.findChildren(QPushButton) \
                + ui.full_menu_widget.findChildren(QPushButton)
    
    for btn in btn_list:
        if index in [5, 6]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
        else:
            btn.setAutoExclusive(True)
# def save_to_excel(fullname, dob, sex, height, weight, phone, insur_number, address, note):
#     filename = os.path.join(DATA_PATH, "Profile_of_Patient.xlsx")
#     fields = ["Full Name", "Day of Birth", "Sex", "Height (cm)", "Weight (kg)", "Phone Number", "Health Insurance Number", "Address", "Note"]
#     row = [fullname, dob, sex, height, weight, phone, insur_number, address, note]

#     # Kiểm tra xem file đã tồn tại chưa
#     if os.path.isfile(filename):
#         df = pd.read_excel(filename)
#         df.loc[len(df)] = row
#     else:
#         df = pd.DataFrame([row], columns=fields)

#     df.to_excel(filename, index=False)

def on_save_button_clicked(ui):
    global error_profile
    fullname = ui.line_fullname.text()
    dob = ui.dateEdit.date().toString("dd/MM/yyyy")
    sex = ui.comboBox.currentText()
    height = ui.line_height.text()
    weight = ui.line_weight.text()
    insur_number = ui.line_insur_number.text()
    address = ui.line_address.text()
    note = ui.line_note.text()
    phone = ui.line_phone_number.text()
    # df = pd.read_excel(os.path.join(DATA_PATH,"Profile_of_Patient.xlsx"))
        
    if error_profile is None:
        error_profile = QtWidgets.QLabel(ui.frame)
        error_profile.setStyleSheet("background-color: rgba(0,0,0,0);color: red")
        font.setPointSize(10)
        error_profile.setFont(font)
    
    if not all([fullname, sex, height, weight, phone, insur_number, address]):
        error_profile.setText("Please input all fields.")
        error_profile.setGeometry(QtCore.QRect(250, 650, 500, 30))
        error_profile.show()          
    elif check_fullname_exists(fullname):
        error_profile.setText("Profile already exists.")
        error_profile.setGeometry(QtCore.QRect(250, 650, 500, 30))
        error_profile.show()
    elif not height.isdigit() or not weight.isdigit():
            error_profile.setText("Height or weight must be integers.")
            error_profile.setGeometry(QtCore.QRect(250, 400, 500, 30))
            error_profile.show()
    else:
        error_profile.deleteLater()
        error_profile = None 
        try:
            username = fullname.replace(" ", "").lower()
            password = phone 
            print(username,password)
            identity = manager.create_and_add_paitent_to_db(cursor, username) 
            # print(str(identity ))         
            save_to_db(fullname, dob, sex, str(height), str(weight),str(phone), str(insur_number), address, note,username,password,identity)
            cursor.execute(f"ALTER TABLE patient_threadmanage ADD COLUMN {username} text")
            cursor.connection.commit()


            # Show a success message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("New profile saved successfully!")
            msg.setWindowTitle("Success")
            msg.exec_()
            # Clear the fields after successful save
            on_clear_button_clicked(ui)
        except Exception as e:
            # Show an error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Failed to save new profile.")
            msg.setInformativeText(str(e))  # Show the error message from the exception
            msg.setWindowTitle("Error")
            msg.exec_()

def on_clear_button_clicked(ui):
    global error_profile
    ui.line_fullname.clear()
    ui.dateEdit.setDate(QtCore.QDate.currentDate())
    ui.comboBox.setCurrentIndex(0)
    ui.line_height.clear()
    ui.line_weight.clear()
    ui.line_phone_number.clear()
    ui.line_insur_number.clear()
    ui.line_address.clear()
    ui.line_note.clear()
    if error_profile is not None:
        error_profile.deleteLater()
        error_profile = None 
def on_combobox_changed(index):
    ui.stackedWidget_2.setCurrentIndex(index)

def on_home_btn_toggled(ui):
    ui.stackedWidget.setCurrentIndex(1)

def on_display_btn_toggled(ui):
     
    ui.stackedWidget.setCurrentIndex(3)
    ui.comboBox_2.setCurrentIndex(0)
    on_combobox_changed(0)
    if not hasattr(ui, 'combobox_connected'):
        ui.comboBox_2.currentIndexChanged.connect(on_combobox_changed)
        ui.combobox_connected = True
        # ui.widget_ave_age.setLayout(QVBoxLayout())
        account_count = get_account_count()
        ui.label_number_doctors.setText(str(account_count))
        patient_count = get_patient_count()
        male_count = get_gender_count('Male')
        female_count = get_gender_count('Female')
        ui.label_number_patients.setText(str(patient_count))
        ui.label_number_male.setText(str(male_count))
        ui.label_number_female.setText(str(female_count))
        if patient_count > 0:
            male_percentage = round((male_count / patient_count) * 100, 2)
            female_percentage = round((female_count / patient_count) * 100, 2)
            ui.label_per_male.setText(f"{str(male_percentage)}")
            ui.label_per_female.setText(f"{str(female_percentage)}")
        patient_ages = get_patient_ages()
        average_age = round(sum(patient_ages) / len(patient_ages),2) if patient_ages else 0
        ui.label_ages.setText(f"{str(average_age)}")
        plot_age_distribution(patient_ages, ui.widget_plot)
        
        # Add patient profiles to comboBox_name
        profiles = get_patient_profiles()
        print(profiles)
        ui.comboBox_name.clear()
        for profile in profiles:
            # print(profile[0])
            ui.comboBox_name.addItem(f"{profile[0]}, {profile[1]}")

        # Update comboBox_date when a profile is selected
        def on_profile_selected():
            global current_user,table_name
            selected_index = ui.comboBox_name.currentIndex()
            selected_profile = profiles[selected_index]
            fullname, _, user = selected_profile
            
            user_account = fullname.replace(' ', '').lower()
            print(user_account,current_user)
            # Kiểm tra xem người dùng hiện tại có quyền truy cập vào hồ sơ này không
            if user_account != current_user and table_name == 'patient_account':
                # Hiển thị pop up cảnh báo
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"Only {fullname} and their doctor are authorized to access this data.")
                msg.setWindowTitle("Warning")
                msg.exec_()
                ui.comboBox_date.clear()
                return

            ui.tables = get_tables(fullname)
            ui.comboBox_date.clear()  # Clear the combobox before adding new items
            for table in ui.tables:
                new_format_str = convert_date_format(table, fullname)
                ui.comboBox_date.addItem(new_format_str)
            patient_details = get_patient_details(fullname)
            if patient_details:
                ui.label_fullname.setText(patient_details['fullname'])
                ui.label_dob.setText(patient_details['dob'])
                ui.label_insur.setText(patient_details['insur_number'])
                ui.label_phone.setText(patient_details['phone'])
                ui.label_sex.setText(patient_details['sex'])
        ui.comboBox_name.activated.connect(on_profile_selected)
        # on_profile_selected()
        x_axis = AxisItem(orientation='bottom')
        y_axis = AxisItem(orientation='left')
        x_axis.setPen('k')  #Black
        y_axis.setPen('k')
        x_axis.setTextPen('k')
        y_axis.setTextPen('k')
        plot_widget = PlotWidget(axisItems={'bottom': x_axis, 'left': y_axis})
        plot_widget.setBackground('w')
        plot_widget.showGrid(True, True, alpha=0.5)
        plot_widget.setYRange(-0.5, 3.5)
        plot_widget.clear()
        data_line = plot_widget.plot([],[],pen=mkPen('r', width=2))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(plot_widget)
        ui.widget_ecg_graph.setLayout(layout)
        def on_start_button_clicked():
            selected_index = ui.comboBox_date.currentIndex()
            table_name = ui.tables[selected_index]
            x, y = get_data_from_table(table_name)
            if len(x)==0 or len(y)==0: 
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("No data available for the selected table.")
                msg.setWindowTitle("Information")
                msg.exec_()
            else:
                start_plot(data_line, plot_widget, x, y,ui.label_47)
        ui.start_button.clicked.connect(on_start_button_clicked)
def on_newprofile_btn_toggled(ui):
    global error_profile, table_name
    if table_name == 'patient_account':
        if not hasattr(ui, 'warning_shown_newprofile') or not ui.warning_shown_newprofile:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Patient accounts are not authorized to view this section.")
            msg.setWindowTitle("Warning")
            msg.exec_()
            ui.warning_shown_newprofile = True
        else:
            ui.warning_shown_newprofile = False        
        return

    ui.stackedWidget.setCurrentIndex(2)
    on_clear_button_clicked(ui)

    if error_profile is not None:
        error_profile.deleteLater()
        error_profile = None     

    if not hasattr(ui, 'save_button_connected'):
        ui.save_button.clicked.connect(lambda: on_save_button_clicked(ui))
        ui.save_button_connected = True

    ui.clear_button.clicked.connect(lambda: on_clear_button_clicked(ui))
def on_uart_btn_toggled(ui):
    global table_name
    if table_name == 'patient_account':
        if not hasattr(ui, 'warning_uart') or not ui.warning_uart:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Patient accounts are not authorized to view this section.")
            msg.setWindowTitle("Warning")
            msg.exec_()
            ui.warning_uart = True
        else:
            ui.warning_uart = False        
        return
    ui.stackedWidget.setCurrentIndex(4)
def homepage_Ui():
    global ui,error_msg,username,password, current_user, table_name
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
        # df = pd.read_csv(os.path.join(DATA_PATH,'Login_Account.csv'))
        is_valid, table_name = check_user_and_password_signin(username, password)
        if is_valid:
            current_user = username
            print(f"Current logged in user: {current_user}")
            print(f"User belongs to: {table_name}")
            ui = sidebar.Ui_MainWindow()
            ui.setupUi(Mainwindow)
            # Mainwindow.setFixedHeight(994)
            # Mainwindow.setFixedWidth(1920) 
            # Mainwindow.resize(1000,600)
            Mainwindow.showMaximized()
            ui.icon_only_widget.hide()
            ui.stackedWidget.setCurrentIndex(1)
            ui.home_btn_2.setChecked(True)
            # # Connect signals to slots
            ui.stackedWidget.currentChanged.connect(lambda: on_stackedWidget_currentChanged(ui, ui.stackedWidget.currentIndex()) if ui.stackedWidget.currentIndex() else None)
            ui.home_btn_1.toggled.connect(lambda: on_home_btn_toggled(ui) if ui.home_btn_1.isChecked() else None)
            ui.home_btn_2.toggled.connect(lambda: on_home_btn_toggled(ui) if ui.home_btn_2.isChecked() else None)
            ui.display_btn_1.toggled.connect(lambda: on_display_btn_toggled(ui) if ui.display_btn_1.isChecked() else None)
            ui.display_btn_2.toggled.connect(lambda: on_display_btn_toggled(ui) if ui.display_btn_2.isChecked() else None)
            ui.newprofile_btn_1.toggled.connect(lambda: on_newprofile_btn_toggled(ui) if ui.newprofile_btn_1.isChecked() else None)
            ui.newprofile_btn_2.toggled.connect(lambda: on_newprofile_btn_toggled(ui) if ui.newprofile_btn_2.isChecked() else None)
            ui.uart_btn_1.toggled.connect(lambda: on_uart_btn_toggled(ui) if ui.uart_btn_1.isChecked() else None)
            ui.uart_btn_2.toggled.connect(lambda: on_uart_btn_toggled(ui) if ui.uart_btn_2.isChecked() else None)
            
            def open_web_and_start_cmd(username, table_name):
                open_web.open_web(username, table_name)
                open_web.start_cmd()

            # Create a new thread for opening web and starting cmd
            thread = threading.Thread(target=open_web_and_start_cmd, args=(username, table_name))
            thread.start()
        else:
            error_msg.setText("Invalid username or password.")
            error_msg.setGeometry(QtCore.QRect(70, 265, 300, 30))
            error_msg.show()
login_Ui()

sys.exit(app.exec_())