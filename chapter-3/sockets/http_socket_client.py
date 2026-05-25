# Sending data through sockets

import socket

# Create socket
s1 = socket.socket()

# Connect to google HTTP server
s1.connect(("google.com", 80))

# Raw HTTP request
request = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"

# Send request
s1.send(request)

# Receive response
response = s1.recv(1024)

# Print decoded response
print(response.decode())

# Close socket
s1.close()
