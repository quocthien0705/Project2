import tkinter as tk
import tkinter.font as font
from tkinter import ttk 
from PIL import Image, ImageTk
import os
import time
import threading
from Check_Internet import check_internet
import pandas as pd

ROOT_PATH      = os.path.dirname(os.path.abspath(__file__))
DATA_PATH      = os.path.join(ROOT_PATH,'..','Data')
def check_credentials(username, password):
    # Check credentials
    df = pd.read_csv(os.path.join(DATA_PATH, 'Login_Account.csv'))
    return any((df['Username'] == username) & (df['Password'] == password))

