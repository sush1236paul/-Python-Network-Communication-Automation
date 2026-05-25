import socket

target = "scanme.nmap.org"
port = 80

# Create socket
s = socket.socket()

# Connect to target
s.connect((target, port))

# Send HTTP request
s.send(b"GET / HTTP/1.1\r\nHost: scanme.nmap.org\r\n\r\n")

# Receive response
banner = s.recv(1024)

# Print response
print(banner.decode())

# Close socket
s.close()
