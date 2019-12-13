#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TCP blocking client demo.
"""

__author__ = 'Ziang Lu'

import socket

# Create an IPv4, TCP socket
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Connect the socket to the server
print("[CLIENT] Connecting to 127.0.0.1:9999...")
s.connect(('127.0.0.1', 9999))

print(s.recv(1024).decode('utf-8'))
for name in ['Michael', 'Tracy', 'Sarah']:
    s.sendall(name.encode('utf-8'))

    print(s.recv(1024).decode('utf-8'))
    # In the server, we deliberately sleep for 1 second before replying, recv()
    # will block here in the client.
s.sendall(b'exit')

# Close the socket
s.close()
print('[CLIENT] Client socket closed')

# Output:
# [CLIENT] Connecting to 127.0.0.1:9999...
# Welcome!
# Hello, Michael
# Hello, Tracy
# Hello, Sarah
# [CLIENT] Client socket closed
