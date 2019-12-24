#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Demo of the TCP server with asyncio for concurrent connections.
"""

__author__ = 'Ziang Lu'

import asyncio
import socket
from typing import Coroutine, Tuple


async def tcp_worker(sock_conn, addr: Tuple[str, int]) -> Coroutine:
    """
    Coroutine to handle TCP connection.
    :param sock_conn: socket
    :param addr: tuple(str, int)
    :return: coroutine
    """
    host, port = addr
    print(f'[SERVER] Connection accepted from {host}:{port}')
    sock_conn.sendall(b'Welcome!')
    # This while-loop is like an "event loop".
    while True:
        # By default, "socket.recv()" is blocking, so the event loop will block
        # here, waiting for some data to come in.
        data = sock_conn.recv(1024)
        await asyncio.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock_conn.sendall(f"Hello, {data.decode('utf-8')}".encode('utf-8'))
    sock_conn.close()
    print(f'[SERVER] Connection from {host}:{port} CLOSED')


##### METHOD 1: With "socket" module #####

# Create an IPv4, TCP socket
server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# Bind the socket to server address "127.0.0.1:9999"
server_sock.bind(('127.0.0.1', 9999))
print('[SERVER] Server bound to 127.0.0.1:9999')

# Let the server socket start listening for connections requests
server_sock.listen()  # Becomes a server socket
print('[SERVER] Server listening for connection...')

try:
    while True:
        sock_conn, addr = server_sock.accept()
        # Schedule an asynchronous coroutine to handle the connection, so that
        # the server is not blocked away from other connections.
        asyncio.run(tcp_worker(sock_conn, addr))
except KeyboardInterrupt:
    # Close the server socket
    server_sock.close()


##### METHOD 2: With "socketserver" module #####

# Simply change one line from before:
# tcp_worker(sock_conn, self.client_address)
# =>
# asyncio.run(tcp_worker(sock_conn, self.client_address))
