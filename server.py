import socket
from datetime import datetime

# Create socket
s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)

print("Server is listening...")
c, addr = s.accept()

print("Client Address :", addr)

# Send current date & time to client
now = datetime.now()
c.send(now.strftime("%d/%m/%Y %H:%M:%S").encode())

# Receive acknowledgement from client
ack = c.recv(1024).decode()
if ack:
    print(ack)

c.close()
