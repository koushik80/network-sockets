import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is the Internet address family IPv4
# SOCK_STREAM is the socket type for TCP
# the protocol tha will be used to transport message
# in the network. (Connection-based socket)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# reuse address, so tat "address already in use"
# -errors could be avoided if program crashes but port remains open


#server.bind(('localhost', 9999))
HOST = 'localhost'
PORT = 9999
server.bind((HOST, PORT))
server.listen()  # number of max. connections as parameter

conn, addr = server.accept()
print("Connection from: " + str(addr))
# The accept() method Python's socket class
# accepts an incoming connection request from a TCP client
# conn is a new socket object usable to
# address is the address bound

connected = True

while connected:  # infine loop
    #message = conn.recv(1024).decode('utf-8')
    if message:
        message = conn.recv(1024).decode()
        print("from connected user: " + str(message))
        message = input(' -> ')
        conn.send(message.encode())  # send mes to the client
        if message == 'quit':
            connected = False

    conn.close()
    # server.close()
