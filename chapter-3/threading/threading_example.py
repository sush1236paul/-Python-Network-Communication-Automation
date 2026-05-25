import socket
import threading

target = "scanme.nmap.org"

ports = [21, 22, 80, 443, 8080]


def scan(port):

    s = socket.socket()

    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} OPEN")

    else:
        print(f"[-] Port {port} CLOSED")

    s.close()


for port in ports:

    t = threading.Thread(target=scan, args=(port,))

    t.start()
