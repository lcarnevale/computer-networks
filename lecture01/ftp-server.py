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
__description__ = 'FTP Server'


import argparse
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

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

    parser.add_argument('-P', '--port',
                        dest='port',
                        help='Port',
                        type=int,
                        default=2121)

    parser.add_argument('-u', '--username',
                        dest='username',
                        help='Define the username',
                        type=str,
                        required=True)

    parser.add_argument('-p', '--password',
                        dest='password',
                        help='Define the password',
                        type=str,
                        required=True)

    parser.add_argument('-f', '--folder',
                        dest='folder',
                        help='Define the FTP folder',
                        type=str,
                        required=True)

    options = parser.parse_args()
    host = options.host
    port = options.port
    username = options.username
    password = options.password
    folder = options.folder

    authorizer = DummyAuthorizer()
    authorizer.add_user(username, password, folder, perm="elradfmwMT")

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Instantiate FTP server class and listen on custom hostname and port
    server = FTPServer((host, port), handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()