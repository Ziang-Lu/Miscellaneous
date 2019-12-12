#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TCP server demo.
"""

__author__ = 'Ziang Lu'

# import concurrent.futures as cf
import socket
import socketserver
import time
from typing import Tuple


def tcp_worker(sock_conn: socket.socket, addr: Tuple[str, int]) -> None:
    """
    Thread function to handle TCP connection.
    :param sock_conn: socket
    :param addr: tuple(str, int)
    :return: None
    """
    host, port = addr
    print(f'[SERVER] Connection accepted from {host}:{port}')
    sock_conn.send(b'Welcome!')
    while True:
        data = sock_conn.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock_conn.send(f"Hello, {data.decode('utf-8')}".encode('utf-8'))
    sock_conn.close()
    print(f'[SERVER] Connection accepted from {host}:{port} CLOSED')


##### METHOD 1: With "socket" module #####


# # Create an IPv4, TCP socket
# server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# # Bind the socket to server address "127.0.0.1:9999"
# server_sock.bind(('127.0.0.1', 9999))
# print('[SERVER] Server bound to 127.0.0.1:9999')

# # Let the server start listening for connections requests
# server_sock.listen()  # Becomes a server socket
# print('[SERVER] Listening for connection...')

# # => Use a thread pool to reuse the thread, and thus improve performance
# with cf.ThreadPoolExecutor(max_workers=50) as pool:
#     try:
#         while True:
#             sock_conn, addr = server_sock.accept()  # Accepted a connection
#             # We want to fire up a thread to handle the connection, so that the
#             # server is not blocked away from other connections.
#             # => Use a thread pool to reuse the thread, and thus improve
#             #    performance
#             pool.submit(tcp_worker, sock_conn, addr)
#     except KeyboardInterrupt:
#         # Close the server socket
#         server_sock.close()


##### METHOD 2: With "socketserver" module #####


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    TCP handler class for our TCP server.
    When a connection is accepted, a thread is fired up to handle it, an object
    of this class is instantiated, and the corresponding handle() method is
    called.
    """

    def handle(self):
        sock_conn = self.request
        # Reuse the "thread" function defined above
        tcp_worker(sock_conn, self.client_address)


# Create a multi-threaded version of TCP server, and bind the server socket to
# server address "127.0.0.1:9999"
server = socketserver.ThreadingTCPServer(
    server_address=('127.0.0.1', 9999), RequestHandlerClass=MyTCPHandler
)
# With ThreadingTCPServer, each connection will have a thread fired up to handle
# it, a RequestHandlerClass object is instantiated, and the corresponding
# handle() method is called.
print('[SERVER] Server bound to 127.0.0.1:9999')

try:
    # Activate the server
    # Let the server start listening for connections requests
    print('[SERVER] Listening for connections...')
    server.serve_forever()
except KeyboardInterrupt:
    # Close the server
    server.server_close()

# Output:
# [SERVER] Server bound to 127.0.0.1:9999
# [SERVER] Listening for connection...
# [SERVER] Connection accepted from 127.0.0.1:56389
# [SERVER] Connection accepted from 127.0.0.1:56389 CLOSED
