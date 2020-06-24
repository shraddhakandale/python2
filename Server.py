import socket
s = socket.socket()
print("socket created")
s.bind(('localhost',9999))
s.listen(3)
print("Waiting for the connections...")
while True:
    c,address = s.accept()
    name = c.recv(1024).decode()
    print("connected with", address,name)
    c.send(bytes('Welcome client','utf-8'))
    c.close()
