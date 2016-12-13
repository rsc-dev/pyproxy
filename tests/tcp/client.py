#!/usr/bin/env python

__author__      = 'Radoslaw Matusiak'
__copyright__   = 'Copyright (c) 2016 Radoslaw Matusiak'
__license__     = 'MIT'
__version__     = '0.1'

import socket
import time

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000
BUFFER_SIZE = 2 ** 10

MESSAGE = "client"

 
def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER_HOST, SERVER_PORT)
    
    client_socket.connect(server_address)

    while True:
        client_socket.sendall('hello_server')
        data = client_socket.recv(BUFFER_SIZE)
    
        print '[*] Server (%s) response: "%s"' % (str(server_address), data)
        
        time.sleep(3)
# end-of-function run_client


if __name__ == '__main__':
    print '[*] Running TCP client...'
    run_client()