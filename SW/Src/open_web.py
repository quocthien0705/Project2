import subprocess
import os
from azure_communication_function import  * 
import webbrowser
import time
import json
def open_web(user_name,table_name):
    with open('paths.json', 'r') as f:
        paths = json.load(f)
    path = paths.get('Video Call')   # replace with your directory
    os.chdir(path)

    command = "npx webpack serve --config webpack.config.js"
    process = subprocess.Popen(command, shell=True)
    path = paths.get('cur_dir')
    os.chdir(path)
    create_token_and_write_to_json(user_name,table_name)
    write_display_names_to_json()
    time.sleep(5)
    webbrowser.open("http://localhost:8080")  # replace with your localhost URL


def start_cmd():
    with open('paths.json', 'r') as f:
        paths = json.load(f)
    path = paths.get('Chat')
    os.chdir(path)
    print(os.getcwd())
    command = "npm run start"
    process = subprocess.run(command, shell=True)
    path = paths.get('cur_dir')
    os.chdir(path)