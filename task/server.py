import socket
#import threading
from person import Person
import pickle


HOST = 'localhost'
PORT = 5050
#ADDR = (HOST, PORT)
#FORMAT = 'utf-8'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

connected = True
p1 = Person('Matti', 50)


def start_server():
    server.listen()
    print(f"Listening at {HOST} on PORT {PORT}")
    while connected:
        client_socket, addr = server.accept()
        print(f'CONNECTION FROM {addr}')
        msg = pickle.dumps(p1)
        client_socket.send(msg)


start_server()
