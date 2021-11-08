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
__description__ = 'HTTP Client'

import urllib3
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
                        help='Define the host',
                        type=str,
                        default='localhost')
    
    parser.add_argument('-P', '--port',
                        dest='port',
                        help='Define the port',
                        type=int,
                        default=8080)

    options = parser.parse_args()
    host = options.host
    port = options.port
    endpoint = 'http://%s:%s' % (host, port)

    http = urllib3.PoolManager()

    # sending GET request
    res = http.request("GET", endpoint)
    print(res.data)

    # sending POST request
    res = http.request("POST", endpoint, fields={"field": "value"})
    print(res.data)

if __name__ == '__main__':
    main()