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

import requests
import argparse

def main():
    description = ('%s\n%s' % (__author__, __description__))
    epilog = ('%s\n%s' % (__credits__, __copyright__))
    parser = argparse.ArgumentParser(
        description = description,
        epilog = epilog
    )

    parser.add_argument('-t', '--token',
                        dest='token',
                        help='Define the token',
                        type=str,
                        required=True)

    parser.add_argument('-c', '--city',
                        dest='city',
                        help='Define the city',
                        type=str,
                        required=True)

    options = parser.parse_args()
    token = options.token
    city = options.city
    host = 'http://api.openweathermap.org/'

    pathname = 'data/2.5/weather?q=%s&appid=%s' % (city, token)
    endpoint = '%s%s' % (host, pathname)
    r = requests.get(endpoint)
    print(r.json())

if __name__ == '__main__':
    main()