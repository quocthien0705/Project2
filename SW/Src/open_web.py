import subprocess
import os
from azure_communication_function import  * 
import webbrowser
def open_web(user_name):
    path = r"D:\HCMUT\huy\PJ2\New folder\Project2\SW\New folder - Copy"  # replace with your directory
    os.chdir(path)

    command = "npx webpack serve --config webpack.config.js"
    process = subprocess.Popen(command, shell=True)
    create_token_and_write_to_json(user_name)
    write_display_names_to_json()
    webbrowser.open("http://localhost:8080")  # replace with your localhost URL