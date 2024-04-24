import subprocess
import os
from azure_communication_function import  * 
import webbrowser
import time
def open_web(user_name,table_name):
    path = r"SW\Src\Video Call"  # replace with your directory
    os.chdir(path)

    command = "npx webpack serve --config webpack.config.js"
    process = subprocess.Popen(command, shell=True)
    create_token_and_write_to_json(user_name,table_name)
    write_display_names_to_json()
    time.sleep(5)
    webbrowser.open("http://localhost:8080")  # replace with your localhost URL
    
    os.chdir('..')

def start_cmd():
    path = r'SW\Src\Chat'
    os.chdir(path)
    print(os.getcwd())
    command = "npm run start"
    process = subprocess.run(command, shell=True)
    os.chdir('..')