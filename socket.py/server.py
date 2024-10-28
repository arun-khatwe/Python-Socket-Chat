import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #bring the ipv4 address of the host
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
  print(f"[NEW CONNECTION] {addr} connected. ")
  
  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode(FORMAT)
      if msg == DISCONNECT_MESSAGE:
        connected = False
      
      print(f"[{addr}] {msg}")
      conn.send("Message received".encode(FORMAT))
  conn.close()
      
def start():
  server.listen()
  print(F"[LISTENING] Server is listening on {SERVER}")
  while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print("[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    
print("[SARTING] server is starting...")
start()