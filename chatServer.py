#Python internet chat room server
#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
socket_array = []
addr_array = []
while True:
    c, addr = s.accept()     # Establish connection with client.
    for x in socket_array:
        x.send("someone has connected")
    socket_array.append(c)
    addr_array.append(addr)
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    print c.recv(1024)
    #s.sendto('test', addr)