import serial.tools.list_ports
from support_function import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit, QWidget, QLabel, QMessageBox,QFileDialog,QDialog,QSizePolicy
from PyQt5.QtCore import QTimer, Qt
from datetime import datetime
from pyqtgraph import PlotWidget, mkPen
from serial_data_receiver import SerialDataReceiver
<<<<<<< HEAD
class SaveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Save ECG Data")
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Please select Full Name or Health Insurance Number of Patient:", self)
        self.label.setFont(QFont("Rockwell",9))
        self.layout.addWidget(self.label)
        self.comboBox = QComboBox(self)
        self.comboBox.setMaxVisibleItems(4)
        # self.comboBox.setFixedWidth(350)
        self.comboBox.setFont(QFont("Rockwell", 10))
        self.comboBox.setStyleSheet("""
            QComboBox {
                border: 1px solid gray;
                border-radius: 3px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
            }

            QComboBox:editable {
                background: white;
            }

            QComboBox:!editable, QComboBox::drop-down:editable {
                background: #D3D3D3;
            }

            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                background: #D3D3D3;
            }

            QComboBox:on {
                padding-top: 3px;
                padding-left: 4px;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }

            QComboBox::down-arrow {
                image: url(:/icon/Icon_Logo/arrow-204-32.ico);
                width: 10px;
                height: 10px;
                margin-right:2px;
                margin-left:2px;
            }
        """)
        self.layout.addWidget(self.comboBox)

        self.saveButton = QPushButton("Save", self)
        self.saveButton.setFont(QFont("Rockwell", 12))
        self.saveButton.setStyleSheet("""
            QPushButton {
                background-color: rgba(21, 122, 110,255);
                color:white;
                border-radius:7px;
            }

            QPushButton:hover {
                background-color: rgba(21, 122, 110,200);
            }

            QPushButton:pressed {
                padding-left:5px;
                padding-top:5px;
                background-color: rgba(17, 98, 87,200);
            }
        """)
        self.saveButton.setFixedSize(100, 40)
        buttonLayout = QHBoxLayout()
        spacerLeft = QWidget()
        spacerLeft.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        spacerRight = QWidget()
        spacerRight.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        buttonLayout.addWidget(spacerLeft)
        buttonLayout.addWidget(self.saveButton)
        buttonLayout.addWidget(spacerRight)

        self.layout.addLayout(buttonLayout)

        self.setFixedSize(480, 130)

class ExportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Export ECG Data to Excel")
        self.layout = QVBoxLayout(self)

        self.label = QLabel("Please select Full Name of Patient:", self)
        self.label.setFont(QFont("Rockwell",9))
        self.layout.addWidget(self.label)

        self.comboBox = QComboBox(self)
        self.comboBox.setMaxVisibleItems(4)
        self.comboBox.setFont(QFont("Rockwell", 10))
        self.comboBox.setStyleSheet("""
            QComboBox {
                border: 1px solid gray;
                border-radius: 3px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
            }

            QComboBox:editable {
                background: white;
            }

            QComboBox:!editable, QComboBox::drop-down:editable {
                background: #D3D3D3;
            }

            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                background: #D3D3D3;
            }

            QComboBox:on {
                padding-top: 3px;
                padding-left: 4px;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }

            QComboBox::down-arrow {
                image: url(:/icon/Icon_Logo/arrow-204-32.ico);
                width: 10px;
                height: 10px;
                margin-right:2px;
                margin-left:2px;
            }
        """)
        self.layout.addWidget(self.comboBox)

        self.tableLabel = QLabel("Please select a table:", self)
        self.tableLabel.setFont(QFont("Rockwell",9))
        self.layout.addWidget(self.tableLabel)

        self.tableComboBox = QComboBox(self)
        self.tableComboBox.setMaxVisibleItems(4)
        self.tableComboBox.setFont(QFont("Rockwell", 10))
        self.tableComboBox.setStyleSheet("""
            QComboBox {
                border: 1px solid gray;
                border-radius: 3px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
            }

            QComboBox:editable {
                background: white;
            }

            QComboBox:!editable, QComboBox::drop-down:editable {
                background: #D3D3D3;
            }

            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                background: #D3D3D3;
            }

            QComboBox:on {
                padding-top: 3px;
                padding-left: 4px;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }

            QComboBox::down-arrow {
                image: url(:/icon/Icon_Logo/arrow-204-32.ico);
                width: 10px;
                height: 10px;
                margin-right:2px;
                margin-left:2px;
            }
        """)
        self.layout.addWidget(self.tableComboBox)

        self.pathLabel = QLabel("Please enter the path to save the Excel file:", self)
        self.pathLabel.setFont(QFont("Rockwell",9))
        self.layout.addWidget(self.pathLabel)

        # Create a horizontal layout
        self.pathLayout = QHBoxLayout()

        self.pathLineEdit = QLineEdit(self)
        self.pathLineEdit.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                border-radius: 7px;
                selection-background-color: darkgray;
            }
        """)
        self.pathLineEdit.setFixedWidth(320)  # Adjust the width as needed
        self.pathLayout.addWidget(self.pathLineEdit)

        self.browseButton = QPushButton("Browse", self)
        self.browseButton.setFont(QFont("Rockwell", 12))
        self.browseButton.setStyleSheet("""
            QPushButton {
                background-color: rgba(2, 195, 154,255);
                color:white;
                border-radius:5px;
            }

            QPushButton:hover {
                background-color: rgba(2, 195, 154,200);
            }

            QPushButton:pressed {
                padding-left:5px;
                padding-top:5px;
                background-color: rgba(0, 115, 90,200);
            }
        """)
        self.browseButton.clicked.connect(self.browse)
        self.browseButton.setFixedWidth(120)  # Adjust the width as needed
        self.pathLayout.addWidget(self.browseButton)

        # Add the horizontal layout to the main layout
        self.layout.addLayout(self.pathLayout)

        self.exportButton = QPushButton("Export", self)
        self.exportButton.setFont(QFont("Rockwell", 12))
        self.exportButton.setStyleSheet("""
            QPushButton {
                background-color: rgba(21, 122, 110,255);
                color:white;
                border-radius:7px;
            }

            QPushButton:hover {
                background-color: rgba(21, 122, 110,200);
            }

            QPushButton:pressed {
                padding-left:5px;
                padding-top:5px;
                background-color: rgba(17, 98, 87,200);
            }
        """)
        self.exportButton.setFixedSize(100, 40)
        buttonLayout = QHBoxLayout()
        spacerLeft = QWidget()
        spacerLeft.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        spacerRight = QWidget()
        spacerRight.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        buttonLayout.addWidget(spacerLeft)
        buttonLayout.addWidget(self.exportButton)
        buttonLayout.addWidget(spacerRight)

        self.layout.addLayout(buttonLayout)

        self.setFixedSize(480, 300)

    def browse(self):
        file_path = QFileDialog.getSaveFileName(self, 'Save File', '', 'Excel Files (*.xlsx)')
        if file_path:
            self.pathLineEdit.setText(file_path[0])

=======
# ROOT_PATH      = os.path.dirname(os.path.abspath(__file__))
#DATA_PATH      = os.path.join(os.path.dirname(os.getcwd()),'..', 'Data')
DATA_PATH = 'd:\\HCMUT\\huy\\PJ2\\New folder\\Project2\\SW\\Data'
>>>>>>> 3fb8c6b4b5c0bc4ff661fc00ef3f38683dcb68a3
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.last_data = None
        self.setWindowTitle("SerialPort")
        self.setGeometry(0, 0, 500, 500)
        self.center_window()
        # self.setWindowIcon(QIcon("vizhport.ico"))

        self.serial_ports = []
        self.baud_rates = ["300", "600", "750", "1200", "2400",
            "4800", "9600", "14400", "19200", "31250", "38400",
            "57600", "74880", "115200", "230400", "250000",
            "460800", "500000", "921600", "1000000", "2000000"]

        self.port_label = QLabel("Serial Ports")
        self.port_dropdown = QComboBox()
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_serial_ports)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_data)
        self.export_button = QPushButton("Export Data to Excel")
        self.export_button.clicked.connect(self.export_data)
        
        self.baudrate_label = QLabel("Baud rate")
        self.baudrate_dropdown = QComboBox()
        self.baudrate_dropdown.addItems(self.baud_rates)
        self.baudrate_dropdown.setCurrentText("115200")

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_serial)

        self.stop_button = QPushButton("Stop")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_serial)

        self.plot_widget = PlotWidget()
        self.plot_widget.setMinimumSize(300, 300)
        self.plot_widget.showGrid(False, True, alpha=0.5)

        self.x = []
        self.y = []
        self.serial_thread = None

        self.setup_ui()
        self.refresh_serial_ports()

    def get_available_serial_ports(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        return ports

    def setup_ui(self):
        widget = QWidget(self)
        self.setCentralWidget(widget)

        main_layout = QVBoxLayout(widget)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.port_label)
        top_layout.addWidget(self.port_dropdown)
        top_layout.addWidget(self.refresh_button)
        top_layout.addWidget(self.save_button)
        top_layout.addWidget(self.export_button)
        top_layout.addSpacing(35)
        top_layout.addWidget(self.baudrate_label)
        top_layout.addWidget(self.baudrate_dropdown)

        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.plot_widget)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addStretch(1)

        main_layout.addLayout(button_layout)

    def refresh_serial_ports(self):
        self.serial_ports = self.get_available_serial_ports()
        self.port_dropdown.clear()
        self.port_dropdown.addItems(self.serial_ports)

    def start_serial(self):
        selected_port = self.port_dropdown.currentText()
        selected_baudrate = int(self.baudrate_dropdown.currentText())

        if not selected_port:
            error_message = "Please select a serial port."
            self.show_message_dialog("Serial Port Error", error_message)
            return

        self.stop_serial()
        self.x = []
        self.y = []

        self.serial_thread = SerialDataReceiver(selected_port, selected_baudrate)
        self.serial_thread.data_received.connect(self.update_graph)
        self.serial_thread.start()

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_serial(self):
        if self.serial_thread and self.serial_thread.isRunning():
            self.serial_thread.stop()
            self.serial_thread.wait()

        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def update_graph(self, data):
        if data != self.last_data:
            self.x.append(len(self.x))
            self.y.append(data)
            pen = mkPen(color="blue", width=2)
            self.plot_widget.plot(self.x, self.y, pen=pen, clear=True)
            self.last_data = data

    def show_message_dialog(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def center_window(self):
        frame = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()

        frame.moveCenter(center_point)
        self.move(frame.topLeft())
    #Function create table store data ecg
    def create_table(self, table_name):
        cursor = connect_to_db()
        cursor.execute(
            f"""
            CREATE TABLE {table_name}(
                X FLOAT,
                Y FLOAT
            )
            """
        )
        cursor.connection.commit()
    def get_patient_profiles(self):
        cursor = connect_to_db()
        cursor.execute("SELECT fullname, insur_number FROM profile_of_patient")
        return cursor.fetchall()

    def save_data(self):
        self.dialog = SaveDialog(self)
        self.dialog.setModal(True)
        self.dialog.show()

        profiles = self.get_patient_profiles()
        for profile in profiles:
            self.dialog.comboBox.addItem(f"{profile[0]}, {profile[1]}")

        def on_save():
            selected_profile = self.dialog.comboBox.currentText()
            if selected_profile:
                fullname, insur_number = selected_profile.split(",")
                now = datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")
                table_name = f'data_ecg_{fullname.replace(" ","")}_{timestamp}'
                self.create_table(table_name)

                cursor = connect_to_db()
                for x, y in zip(self.x, self.y):
                    cursor.execute(
                        f"""
                        INSERT INTO {table_name}(
                            X,
                            Y
                        )
                        VALUES (%s,%s)
                        """, 
                        (x, y)
                    )
                cursor.connection.commit()
                self.show_message_dialog("Save Data", "Save data successfully")
                self.dialog.close()

        self.dialog.saveButton.clicked.connect(on_save)
    def export_to_excel(self, table_name, file_path):
        cursor = connect_to_db()
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, cursor.connection)
        df.to_excel(file_path, index=False)   
    def export_data(self):
        self.export_dialog = ExportDialog(self)
        self.export_dialog.setModal(True)
        self.export_dialog.show()

        profiles = self.get_patient_profiles()
        for profile in profiles:
            self.export_dialog.comboBox.addItem(f"{profile[0]}, {profile[1]}")

        def on_profile_selected():
            selected_profile = self.export_dialog.comboBox.currentText()
            if selected_profile:
                fullname, _ = selected_profile.split(",")
                print(fullname)
                tables = get_tables(fullname)
                print(tables)
                self.export_dialog.tableComboBox.clear()  # Clear the combobox before adding new items
                for table in tables:
                    self.export_dialog.tableComboBox.addItem(table)

        self.export_dialog.comboBox.activated.connect(on_profile_selected)

        # Call on_profile_selected once to update tableComboBox for the currently selected profile
        on_profile_selected()

        def on_export():
            selected_table = self.export_dialog.tableComboBox.currentText()
            file_path = self.export_dialog.pathLineEdit.text()  # Get the file path from pathLineEdit
            if selected_table and file_path:  # Check if both selected_table and file_path are not empty
                self.export_to_excel(selected_table, file_path)
                self.show_message_dialog("Export Data", "Export data successfully")
                self.export_dialog.close()

        self.export_dialog.exportButton.clicked.connect(on_export)