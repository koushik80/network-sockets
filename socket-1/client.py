import socket

HOST = 'localhost'
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(input("Enter message:".encode('utf-8')))

client.close()
