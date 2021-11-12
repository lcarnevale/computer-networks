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


import json
import argparse
import requests


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
  protocol = 'http://'
  hostname = '%s:%s' % (host, port)

  print('>> create two new products')
  pathname = '/products'
  url = '%s%s%s' % (protocol, hostname, pathname)
  body = json.dumps( {"pizza": 1, "water": 6} )
  headers = {"Content-Type": "application/json"}
  r = requests.post(url, data=body, headers=headers)
  print(r.text)

  print('>> create an existing product')
  pathname = '/products'
  url = '%s%s%s' % (protocol, hostname, pathname)
  body = json.dumps( {"water": 6} )
  headers = {"Content-Type": "application/json"}
  r = requests.post(url, data=body, headers=headers)
  print(r.text)

  print('>> list all products')
  pathname = '/products'
  url = '%s%s%s' % (protocol, hostname, pathname)
  r = requests.get(url)
  print(r.text)

  print('>> update a product')
  pathname = '/products/pizza'
  url = '%s%s%s' % (protocol, hostname, pathname)
  body = '2'
  headers = {"Content-Type": "text/plain"}
  r = requests.put(url, data=body, headers=headers)
  print(r.text)

  print('>> delete a product')
  pathname = '/products/water'
  url = '%s%s%s' % (protocol, hostname, pathname)
  r = requests.delete(url)
  print(r.text)

  print('>> list all products')
  pathname = '/products'
  url = '%s%s%s' % (protocol, hostname, pathname)
  r = requests.get(url)
  print(r.text)

if __name__ == '__main__':
  main()
