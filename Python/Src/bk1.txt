import tkinter as tk
import tkinter.font as font
from tkinter import ttk 
from PIL import Image, ImageTk
import os
import time
import threading
import pandas as pd
from Check_Internet import check_internet
from Check_credentials import check_credentials

# Path Defined
ROOT_PATH      = os.path.dirname(os.path.abspath(__file__))
DATA_PATH      = os.path.join(ROOT_PATH,'..','Data')
ICON_LOGO_PATH = os.path.join(ROOT_PATH,'..','Icon_Logo')

# Global Variables
username_entry = None
password_entry = None
login_frame = None

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if check_credentials(username, password):
        # Clear all widgets in root
        for widget in root.winfo_children():
            widget.destroy()
        
        # Display success message
        success_label = tk.Label(root, text='Login Successfully', font=('Rockwell Light', 20,'bold'))
        success_label.place(x=center_x, y=center_y, anchor='center')
    else:
        # Display error message
        error_label1 = tk.Label(login_frame, text='The username or password is incorrect.', fg='red',font=('Rockwell Light',12))
        error_label2 = tk.Label(login_frame, text='Please try again.', fg='red',font=('Rockwell',12))
        error_label1.grid(row=5, columnspan = 2)
        error_label2.grid(row=6, columnspan = 2)
# GUI
root = tk.Tk()
root.title('Health Monitoring System')
root.iconbitmap(os.path.join(ICON_LOGO_PATH, 'healthcare.ico'))
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
center_x = x // 2
center_y = y // 2
root.geometry('{0}x{1}+0+0'.format(x,y))
root.state('zoomed')

def display_no_internet_ui():
    image_path = os.path.join(ICON_LOGO_PATH, 'no-internet.png')
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root)
    image_label.image = photo  # lưu trữ tham chiếu đến hình ảnh
    image_label.config(image=photo)
    image_label.place(x=center_x, y=center_y - 60, anchor='center')
    
    row1 = tk.Label(root, text='No Internet connection.', fg = 'red', font = ('Rockwell Light',16))
    row1.place(x=center_x, y=center_y, anchor='center')
    
    row2 = tk.Label(root, text='Please check your Internet connection and try again.', fg = 'black', font = ('Rockwell Light',16))
    row2.place(x=center_x, y=center_y + 30, anchor='center')

def display_login_ui():
    global username_entry, password_entry, login_frame

    login_frame = ttk.Frame(root)
    login_frame.place(x=center_x, y= center_y-30, anchor= 'center', width = 330,height=380)
    login_frame.config(borderwidth=2, relief='solid')
    
    title_label = tk.Label(login_frame, text="Login", font=('Rockwell Light', 24,'bold'),justify='center')
    title_label.grid(row=0, columnspan=3,pady=(30,40))
    
    username_label = tk.Label(login_frame, text='Username:', font=('Rockwell Light', 16))
    username_label.grid(row=3, column=0, sticky="w",pady=(0,20),padx=(10,0))
    username_entry = tk.Entry(login_frame, font=('Rockwell Light', 13), width= 20,bd=0)
    username_entry.grid(row=3, column=1, sticky="w",pady=(0,20),padx=(10,10))

    
    password_label = tk.Label(login_frame, text='Password:', font=('Rockwell Light', 16))
    password_label.grid(row=4, column=0, sticky="w",pady=(0,20),padx=(10,0))
    password_entry = tk.Entry(login_frame, font=('Rockwell Light', 13), show="•", width= 20,bd=0)
    password_entry.grid(row=4, column=1, sticky="w",pady=(0,20),padx=(10,10))
    
        
    login_button = tk.Button(login_frame, text='Log in', command=login, width= 20,font=('Rockwell Light', 10))
    login_button.grid(row=7, columnspan=2)

def update_ui():
    current_state = None
    while True:
        internet_connected = check_internet()
        if internet_connected != current_state:
            # Clear all widgets in root
            for widget in root.winfo_children():
                widget.destroy()
            
            if internet_connected:
                display_login_ui()
            else:
                display_no_internet_ui()
            
            current_state = internet_connected
        
        time.sleep(1)  # Check every 5 seconds
        
threading.Thread(target=update_ui).start()

root.mainloop()
