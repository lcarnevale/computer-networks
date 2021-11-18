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
                        help='Define the host',
                        type=str,
                        default='localhost')

    parser.add_argument('-P', '--port',
                        dest='port',
                        help='Define the port',
                        type=int,
                        default=2121)

    parser.add_argument('-u', '--user',
                        dest='user',
                        help='Define the user',
                        type=str,
                        required=True)

    parser.add_argument('-d', '--directory',
                        dest='directory',
                        help='Define the directory',
                        type=str,
                        required=True)

    parser.add_argument('-v', '--verbose',
                        dest='verbose',
                        help='Define the verbosity',
                        type=bool,
                        default=True)

    options = parser.parse_args()
    host = options.host
    port = options.port
    user = options.user
    directory = options.directory
    password = input("Type your password and press enter: ")

    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, directory, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "pyftpdlib based ftpd ready."

    address = (host, port)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main()