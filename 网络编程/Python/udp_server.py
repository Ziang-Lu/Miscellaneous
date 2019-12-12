#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UDP server demo.
"""

__author__ = 'Ziang Lu'

# import socket
import socketserver


##### METHOD 1: With "socket" module #####


# # Create an IPv4, UDP socket
# s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# # Bind the socket to server address "127.0.0.1:9999"
# s.bind(('127.0.0.1', 9999))
# print('[SERVER] Server bound to 127.0.0.1:9999')

# # No need to listen for connection

# try:
#     while True:
#         data, addr = s.recvfrom(1024)
#         host, port = addr
#         # No firing up a new thread to handle the request here, since UDP simply
#         # receives the data, and directly dumps back the new data
#         print(f'[SERVER] Received from {host}:{port}')
#         s.sendto(f"Hello, {data.decode('utf-8')}".encode('utf-8'), addr)
# except KeyboardInterrupt:
#     # Close the socket
#     s.close()


##### METHOD 2: With "socketserver" module #####


class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    UDP handler class for our UDP server.
    When a connection is accepted, an object of this class is instantiated, and
    the corresponding handle() method is called.
    """

    def handle(self):
        data, sock_conn = self.request
        host, port = self.client_address
        # No firing up a new thread to handle the request here, since UDP simply
        # receives the data, and directly dumps back the new data
        print(f'[SERVER] Received from {host}:{port}')
        sock_conn.sendto(
            f"Hello, {data.decode('utf-8')}".encode('utf-8'),
            self.client_address
        )


# Create a UDP server, and bind the server socket to server address
# "127.0.0.1:9999"
server = socketserver.UDPServer(
    server_address=('127.0.0.1', 9999), RequestHandlerClass=MyUDPHandler
)
print('[SERVER] Server bound to 127.0.0.1:9999')

try:
    # Activate the server
    server.serve_forever()
except KeyboardInterrupt:
    # Close the server
    server.server_close()


# Output:
# [SERVER] Server bound to 127.0.0.1:9999
# [SERVER] Received from 127.0.0.1:50351
# [SERVER] Received from 127.0.0.1:50351
# [SERVER] Received from 127.0.0.1:50351
