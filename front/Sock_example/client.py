#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'GET /index.php/user/list?limit=20 HTTP/1.0\r\n\r\n')
    data = s.recv(1024)

print('Received', repr(data))
