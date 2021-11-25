# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2021, FCRlab at University of Messina'
__author__ = 'Lorenzo Carnevale <lcarnevale@unime.it>'
__credits__ = ''
__description__ = 'HTTP Client implementation over TCP'


import time
import socket
import argparse


def connect(host, port):
    """Connection
    
    Args:
        host(str): destination hostname
        port(int): destination port
    
    Returns:
        the created socket
    """
    # IPv4 address family over TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print('Socket status after connection %s' % (s))
    return s

def post(sock, buffer_size, body):
    """POST request

    Args:
        sock(socket.socket): socket object
        buffer_size(int): maximum size of received message buffer
        body(str): HTTP body
    """
    header = 'POST /products HTTP/1.1\r\n' \
            'Host: localhost:8080\r\n' \
            'Content-Type: application/json\r\n' \
            'Content-Length: %s\r\n' \
            '\r\n' % ( len(body) )

    request = header + body
    # s.send(b'POST /products HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nContent-Type: application/json\r\nContent-Length: 24\r\n\r\n{"pizza": 1, "water": 6}')
    sock.send( request.encode())

    response = sock.recv(buffer_size)
    while len(response) > 0:
        print(response)
        response = sock.recv(buffer_size)

def get(sock, buffer_size):
    """GET request
    
    Args:
        sock(socket.socket): socket object
        buffer_size(int): maximum size of received message buffer
    """
    request = 'GET /products HTTP/1.1\r\n' \
            'Host: localhost:8080\r\n' \
            '\r\n'
    sock.send( request.encode() )

    response = sock.recv(buffer_size)
    while len(response) > 0:
        print(response)
        response = sock.recv(buffer_size)

def put(sock, buffer_size, param, body):
    """PUT request

    Args:
        sock(socket.socket): socket object
        buffer_size(int): maximum size of received message buffer
        param(str): parameter of pathname
        body(str): HTTP body
    """
    header = 'PUT /products/%s HTTP/1.1\r\n' \
            'Host: localhost:8080\r\n' \
            'Content-Type: text/plain\r\n' \
            'Content-Length: %s\r\n' \
            '\r\n' % ( param, len(body) )

    request = header + body
    sock.send( request.encode())

    response = sock.recv(buffer_size)
    while len(response) > 0:
        print(response)
        response = sock.recv(buffer_size)

def delete(sock, buffer_size, param):
    """DELETE request

    Args:
        sock(socket.socket): socket object
        buffer_size(int): maximum size of received message buffer
        param(str): parameter of pathname
    """
    header = 'DELETE /products/%s HTTP/1.1\r\n' \
            'Host: localhost:8080\r\n' \
            '\r\n' % ( param )

    request = header + ''
    sock.send( request.encode())

    response = sock.recv(buffer_size)
    while len(response) > 0:
        print(response)
        response = sock.recv(buffer_size)

def main():
    description = ('%s\n%s' % (__author__, __description__))
    epilog = ('%s\n%s' % (__credits__, __copyright__))
    parser = argparse.ArgumentParser(
        description = description,
        epilog = epilog
    )

    parser.add_argument('-H', '--host',
                        dest='host',
                        help='Hostname',
                        type=str,
                        default='localhost')

    parser.add_argument('-p', '--port',
                        dest='port',
                        help='Port',
                        type=int,
                        default=8080)

    options = parser.parse_args()
    
    host = options.host
    port = options.port
    buffer_size = 1024

    hostname = socket.gethostname()
    print('My hostname is %s' % ( hostname ))
    print('My address is %s' %( socket.gethostbyname(hostname) ))

    s = connect(host, port)
    print('>> create two new products')
    post(s, buffer_size, '{"pizza": 1, "water": 6}')
    s.close()
    time.sleep(2) # only to follow the results on prompt in real-time

    s = connect(host, port)
    print('>> create an existing product')
    post(s, buffer_size, '{"water": 6}')
    s.close()
    time.sleep(2) # only to follow the results on prompt in real-time

    s = connect(host, port)
    print('>> list all products')
    get(s, buffer_size)
    s.close()
    time.sleep(2) # only to follow the results on prompt in real-time

    s = connect(host, port)
    print('>> update a product')
    put(s, buffer_size, 'pizza', '2')
    s.close()
    time.sleep(2) # only to follow the results on prompt in real-time

    s = connect(host, port)
    print('>> delete a product')
    delete(s, buffer_size, 'water')
    s.close()
    time.sleep(2) # only to follow the results on prompt in real-time

    s = connect(host, port)
    print('>> list all products')
    get(s, buffer_size)
    s.close()
    time.sleep(2) # only to follow the results on prompt in real-time

if __name__ == '__main__':
    main()