import socket

s = socket.socket()
host = '172.19.73.56'
port = 12345

s.connect((host,port))

while True:
    c = s.recv(1024)
    if c != "":
        print c