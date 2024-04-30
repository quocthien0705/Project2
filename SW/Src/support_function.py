import numpy as np
import scipy.signal 
import pandas as pd
import psycopg2 as ps
import pywt
from biosppy.signals import ecg
from datetime import datetime
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
from pyqtgraph import ScatterPlotItem
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QSizePolicy,QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os 
import json
# from GUI import current_peak_plot
#Function connect to database
current_peak_plot = None
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
def insert_new_user(username_signup, password_signup, email,identity):
    cursor = connect_to_db()
    cursor.execute(
        """
        INSERT INTO user_account(
            user_name,
            password,
            email,
            identity
        )
        VALUES (%s,%s,%s,%s)
        """, 
        (username_signup, password_signup, email, identity)
    )
    cursor.connection.commit()
#Function check username and password when login
def check_user_and_password_signin(username, password):
    cursor = connect_to_db()
    
    # Kiểm tra trong bảng user_account
    cursor.execute(
        """
        SELECT * FROM user_account
        WHERE user_name = %s AND password = %s
        """, 
        (username, password)
    )
    result = cursor.fetchone()
    if result is not None:
        return True, 'user_account'
    
    # Kiểm tra trong bảng patient_account
    cursor.execute(
        """
        SELECT * FROM patient_account
        WHERE user_name = %s AND password = %s
        """, 
        (username, password)
    )
    result = cursor.fetchone()
    if result is not None:
        return True, 'patient_account'
    
    return False, None

#Function to insert new patient profile   
def save_to_db(fullname, dob, sex, height, weight, phone, insur_number, address, note,username, password,identity):
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


    

    cursor.execute(
        """
        INSERT INTO patient_account(
            user_name,
            password,
            identity
        )
        VALUES (%s,%s,%s)
        """, 
        (username, password,identity)
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
#Count account
def get_account_count():
    cursor = connect_to_db()
    cursor.execute("SELECT COUNT(*) FROM user_account")
    result = cursor.fetchone()
    if result is not None:
        return result[0]
    else:
        return 0

#Count patient
def get_patient_count():
    cursor = connect_to_db()
    cursor.execute("SELECT COUNT(*) FROM profile_of_patient")
    result = cursor.fetchone()
    if result is not None:
        return result[0]
    else:
        return 0
#Count patient's gender
def get_gender_count(gender):
    cursor = connect_to_db()
    cursor.execute(
        """
        SELECT COUNT(*) FROM profile_of_patient
        WHERE sex = %s
        """, 
        (gender,)
    )
    result = cursor.fetchone()
    if result is not None:
        return result[0]
    else:
        return 0
    
def calculate_age(birth_date):
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#Function get ages of patients
def get_patient_ages():
    cursor = connect_to_db()
    cursor.execute("SELECT dob FROM profile_of_patient")
    result = cursor.fetchall()
    if result is not None:
        ages = [calculate_age(datetime.strptime(row[0], '%d/%m/%Y')) for row in result]
        return ages
    else:
        return []

#Function plot average ages
def plot_age_distribution(ages, widget):
    age_counts = [ages.count(i) for i in range(1, 111)]
    plot_widget = pg.PlotWidget()
    plot_widget.setBackground('w')
    plot_widget.setLabel('left', 'Number of Patients')
    plot_widget.setLabel('bottom', 'Ages')
    plot_widget.showGrid(x=True, y=True)
    # Create a bar graph with pink color and no border
    bar_item = pg.BarGraphItem(x=range(1, 111), height=age_counts, width=1, brush='pink')
    plot_widget.addItem(bar_item)
    
    if widget.layout() is not None:
        widget.layout().addWidget(plot_widget)
    else:
        layout = QVBoxLayout()
        layout.addWidget(plot_widget)
        widget.setLayout(layout)
    
def get_patient_profiles():
    cursor = connect_to_db()
    cursor.execute("SELECT fullname, insur_number, phone FROM profile_of_patient")
    return cursor.fetchall()

#Convert date
def convert_date_format(table, fullname):
    timestamp_str = table.replace(f'data_ecg_{fullname.replace(" ","").lower()}_', '')
    # Convert the timestamp to the new format
    date_str = timestamp_str[:8]
    time_str = timestamp_str[9:]
    new_format_str = f"{date_str[6:8]}/{date_str[4:6]}/{date_str[:4]}, {time_str[:2]}-{time_str[2:4]}-{time_str[4:]}"
    return new_format_str

#Get patient details
def get_patient_details(fullname):
    cursor = connect_to_db()
    cursor.execute("SELECT fullname, dob, sex, phone, insur_number FROM profile_of_patient WHERE fullname = %s", (fullname,))
    result = cursor.fetchone()
    if result is not None:
        return {
            'fullname': result[0],
            'dob': result[1],
            'sex': result[2],
            'phone': result[3],
            'insur_number': result[4]
        }
    else:
        return None
    
def get_data_from_table(table_name):
    cursor = connect_to_db()
    cursor.execute(f"SELECT X, Y FROM {table_name}")
    data = cursor.fetchall()
    x_values = [row[0] for row in data]
    y_values = [row[1] for row in data]
    # Load your ECG data
    data = pd.DataFrame({'X': x_values, 'Y': y_values})

    coeffs = pywt.wavedec(data['Y'].values.squeeze(), 'db4', level=8)

    # Set the detail coefficients at the last two levels to zero
    coeffs[-1] *= 0.5
    coeffs[-2] *= 0.5

    # Apply the inverse DWT to get the filtered signal
    y_values_filtered = pywt.waverec(coeffs, 'db4')

    # Trim y_values_filtered to the same length as x_values
    y_values_filtered = y_values_filtered[:len(x_values)]

    peaks, _ = scipy.signal.find_peaks(y_values_filtered, height=2.2, distance=50)
    k = 60 / (x_values[peaks[10]] - x_values[peaks[9]])
    # print(round(k))

    y_values_filtered = scipy.signal.medfilt(y_values_filtered.squeeze(), kernel_size=3)

    return x_values, y_values_filtered


def start_plot(data_line, plot_widget, x, y,label_47):
    # global current_peak_plot
    current_index = 0
    peaks, _ = scipy.signal.find_peaks(y, height=2.5)  # detect peaks
    # peak_plot = ScatterPlotItem(size=20, pen=pg.mkPen(None), brush=pg.mkBrush(0, 255, 0, 120), symbol='x') 
    plotted_peaks_x = []
    plotted_peaks_y = []
    heart_rates = []  # list to store heart rates

    def update_plot():
        nonlocal current_index
        label_47.setText("00")
        current_index += 1
        if current_index > len(x) - 2000:
            # peak_plot.setData(plotted_peaks_x, plotted_peaks_y)  # plot all peaks
            timer.stop()  # Dừng QTimer khi đến điểm cuối của dữ liệu
            # Calculate heart rate
            for i in range(1, len(plotted_peaks_x)):
                dt = plotted_peaks_x[i] - plotted_peaks_x[i-1]
                heart_rate = 60 / dt
                heart_rates.append(heart_rate)
            avg_heart_rate = round(np.mean(heart_rates[1:])*200)
            print(f"Heart rate : {avg_heart_rate} bpm")
            label_47.setText(f"{avg_heart_rate}")
            try:
                ecg.ecg(signal=y*4096/3.3, sampling_rate=1/0.006, show=True,interactive=False)
            except:
                print('Warning when plot ECG Summary')
            return
        data_line.setData(x[:current_index+2000], y[:current_index+2000])
        plot_widget.setXRange(x[current_index], x[current_index] + 2000)
        plot_widget.setYRange(min(y), max(y))
        # store detected peaks
        peak_indices = [i for i in peaks if current_index <= i < current_index + 2000]
        for peak_index in peak_indices:
            plotted_peaks_x.append(x[peak_index])
            plotted_peaks_y.append(y[peak_index])

    # Xóa peak_plot hiện tại (nếu có) trước khi thêm peak_plot mới
    # if current_peak_plot is not None:
    #     plot_widget.removeItem(current_peak_plot)
    # plot_widget.addItem(peak_plot)
    # current_peak_plot = peak_plot  # Cập nhật peak_plot hiện tại
    timer = QtCore.QTimer()
    timer.setInterval(3)  # in milliseconds
    timer.timeout.connect(update_plot)
    timer.start()
    
def search_dir(names, folder_name):
    file_paths = {os.path.splitext(name)[0]: None for name in names}
    dir_paths = {os.path.splitext(name)[0]: None for name in names}
    
    for folder, _, files in os.walk(folder_name):
        for name in names:
            if name in files and file_paths[os.path.splitext(name)[0]] is None:
                file_paths[os.path.splitext(name)[0]] = os.path.join(folder, name)

    for folder, subfolders, _ in os.walk(folder_name):
        for name in names:
            if name in subfolders and dir_paths[os.path.splitext(name)[0]] is None:
                dir_paths[os.path.splitext(name)[0]] = os.path.join(folder, name)
                
    paths = {os.path.splitext(name)[0]: file_paths.get(os.path.splitext(name)[0]) or dir_paths.get(os.path.splitext(name)[0]) for name in names}
                
    return paths

def write_path_to_json():
    names = ["appsettings.json", "display_names.json", "token_data.json", "Chat", "Video Call"]
    folder_name = os.path.dirname(os.path.abspath(__file__))
    paths = search_dir(names, folder_name)
    paths['cur_dir'] = os.path.dirname(os.path.abspath(__file__))
    with open('paths.json', 'w') as f:
        json.dump(paths, f, ensure_ascii=False, indent=4)