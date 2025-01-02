import socket

s = socket.socket()
port = 12345

s.bind(('192.168.1.150',port))

print("i am server in listening mode")
s.listen(5)

connection, addr = s.accept()
print("connection from ", addr)

message = connection.recv(1024)
print(message)

connection.close()

input("pause")
