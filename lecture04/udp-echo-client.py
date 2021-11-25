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
__description__ = 'ECHO Client implementation over UDP'

import socket
import argparse

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
                        default=65432)

    options = parser.parse_args()
    
    host = options.host    # By default it is the standard loopback interface address (localhost)
    port = options.port    # Port to listen on (non-privileged ports are > 1023)
    buffer_size = 1024

    # IPv4 address family over UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = input("Type you message - ")
        s.sendto(str.encode(message), (host, port))
        message_back, server_address = s.recvfrom(buffer_size)
        server_host, server_port = server_address

    print('Received message \'%s\' back from server %s:%s' % (message_back.decode(), server_host, server_port))

if __name__ == '__main__':
    main()