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
        conn, addr = server.accept()
        print(f'CONNECTION FROM {addr}')
        msg = pickle.dumps(p1)
        conn.send(msg)

        client_msg = conn.recv(1024)
        if client_msg:
            client_msg = client_msg.loads(msg)
            client_msg.print_person()


start_server()
