import socket
import pickle

HOST = 'localhost'
PORT = 5050


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

connected = True

while connected:
    msg = client.recv(1024)
    if msg:
        msg = pickle.loads(msg)
        msg.print_person()
        connected = False
