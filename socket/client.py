import socket

s = socket.socket()

port = 12345 

ip = "server ip"

s.connect((ip,port))
print("connected to server")

s.send(b"Hello server , i am client")

s.close()

input("pause")