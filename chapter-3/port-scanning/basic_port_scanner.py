import socket

target = input("Enter target IP or domain: ")

print(f"\nScanning target: {target}\n")

# Common ports
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443]

for port in ports:

    s = socket.socket()

    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    else:
        print(f"Port {port} is CLOSED")

    s.close()
