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
__description__ = 'HTTP Server'

import os
import argparse
from http.server import HTTPServer, CGIHTTPRequestHandler


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
                        default='')
    
    parser.add_argument('-P', '--port',
                        dest='port',
                        help='Define the port',
                        type=int,
                        default=8080)

    parser.add_argument('-p', '--path',
                        dest='path',
                        help='Define the path',
                        type=str,
                        default='.')

    options = parser.parse_args()
    host = options.host
    port = options.port
    path = options.path

    os.chdir(path)
    server_object = HTTPServer(server_address=(host, port), RequestHandlerClass=CGIHTTPRequestHandler)
    server_object.serve_forever()    

if __name__ == '__main__':
    main()