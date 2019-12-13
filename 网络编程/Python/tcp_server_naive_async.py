#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Demo of the TCP server with naive async implementation based on a
"selectors"-based event loop, for concurrent connections.
"""

import selectors
import socket
import time
import types

# Create an IPv4, TCP socket
server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# Bind the socket to server address "127.0.0.1:9999"
server_sock.bind(('127.0.0.1', 9999))
print('[SERVER] Server bound to 127.0.0.1:9999')

# Let the server start listening for connections requests
server_sock.listen()  # Becomes a server socket
print('[SERVER] Listening for connection...')

# Set to non-blocking mode
server_sock.setblocking(False)

selector = selectors.DefaultSelector()
# Register the server socket to monitor for its read readiness
selector.register(server_sock, selectors.EVENT_READ, data=None)


def accept_wrapper(server_sock: socket.socket) -> None:
    """
    Wrapper function for the given server socket to accept a new connection and
    do some initialization stuff.
    :param server_sock: socket
    :return: None
    """
    # The given server socket is ready to accept a new connection.
    # 1. Get the connection socket
    sock_conn, addr = server_sock.accept()
    host, port = addr
    print(f'[SERVER] Connection accepted from {host}:{port}')
    # 2. Set the connection socket as non-blocking
    sock_conn.setblocking(False)

    # 3. Prepare the initial data for this connection
    conn_data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'Welcome')
    # 4. Register the connection socket to monitor for both its read rediness
    #    and write readiness, as well as saving that data for this connection
    selector.register(
        sock_conn, selectors.EVENT_READ | selectors.EVENT_WRITE, data=conn_data
    )


def serve_conn(sock_conn: socket.socket, events_mask,
               conn_data: types.SimpleNamespace) -> None:
    """
    Serves the given socket connection for the given events, with the given
    corresponding connection data.
    :param sock_conn: socket
    :param events_mask:
    :param conn_data: SimpleNamespace
    :return: None
    """
    if events_mask & selectors.EVENT_READ:
        data = sock_conn.recv(1024)
        if data:
            conn_data.outb += b'Hello, ' + data
            time.sleep(1)
        else:
            host, port = sock_conn.getpeername()
            print(f'[SERVER] Connection accepted from {host}:{port} CLOSED')
            selector.unregister(sock_conn)
            sock_conn.close()
    if events_mask & selectors.EVENT_WRITE:
        if conn_data.outb:
            sent = sock_conn.send(conn_data.outb)
            conn_data.outb = conn_data.outb[sent:]


try:
    while True:
        events = selector.select(timeout=None)  # Still block here
        for key, events_mask in events:
            if key.data is None:
                # Meaning that the socket is the server socket itself, ready to
                # accept a new connection
                server_sock = key.fileobj
                # Accept the connection, and do some initialization stuff
                accept_wrapper(server_sock)
            else:
                # Meaning that the socket is a connection socket, ready to read
                # or write data, depending on the corresponding event mask
                sock_conn = key.fileobj
                conn_data = key.data
                # Let the server serve this connection
                serve_conn(key, events_mask, conn_data)
except KeyboardInterrupt:
    # Clean-up work
    selector.close()
    server_sock.close()
