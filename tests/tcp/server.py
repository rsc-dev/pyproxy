#!/usr/bin/env python

__author__      = 'Radoslaw Matusiak'
__copyright__   = 'Copyright (c) 2016 Radoslaw Matusiak'
__license__     = 'MIT'
__version__     = '0.1'

import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8888
BUFFER_SIZE = 2 ** 10

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    
    conn, addr = server_socket.accept()
    
    while True:
        data = conn.recv(BUFFER_SIZE)
        
        if not data:
            break
        
        print '[*] Received data ("%s") from client (%s)' % (data, str(addr))
        conn.sendall(data)
# end-of-function run_server


if __name__ == '__main__':
    print '[*] Running TCP server on %s:%d...' % (SERVER_HOST, SERVER_PORT)
    run_server()
    