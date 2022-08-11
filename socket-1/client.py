import socket

HOST = 'localhost'
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))  # connect to the server
# message = input(" -> ")  # take input

while True:
    msg = input("Enter message:")  # take input
    client.send(msg.encode())  # send message
    # message = client.recv(1024).decode()  # receive response
    print('Received from server: ' + message)
    if msg == 'quit':  # show in terminal
        break

    # client.close()
