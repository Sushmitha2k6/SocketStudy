import socket

# Create socket
s = socket.socket()
s.connect(('localhost', 8000))

# Receive date/time from server
data = s.recv(1024).decode()
print("Date and Time from server:", data)

# Send acknowledgement back
s.send("acknowledgement recieved from the server".encode())

s.close()
