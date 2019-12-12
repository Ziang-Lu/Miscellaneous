#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UDP client demo.
"""

import socket

# Create an IPv4, UDP socket
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# No need to connect the socket to the server

for name in ['Michael', 'Tracy', 'Sarah']:
    s.sendto(name.encode('utf-8'), ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))

# Close the socket
s.close()
print('[CLIENT] Client socket closed')

# Output:
# Hello, Michael
# Hello, Tracy
# Hello, Sarah
# [CLIENT] Client socket closed
