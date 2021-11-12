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


import json
import argparse
from bottle import run
from bottle import request, response
from bottle import post, get, put, delete


data = {} # better if stored within a file


@post('/products')
def create_product():
  """Handles product creation"""
  try:
    body = json.loads( request.body.read() )
    if products_exist(body):
      raise KeyError
    data.update(body)
    response.status = 200 # OK
  except KeyError:
    response.status = 409 # Conflict
  except Exception:
    response.status = 500 # Internal Server Error
  response.headers['Content-Type'] = 'application/json'
  return json.dumps(data)

def products_exist(products):
  return any(x in products.keys() for x in data.keys())

@get('/products')
def list_products():
  """Handles product listing"""
  response.headers['Content-Type'] = 'application/json'
  response.headers['Cache-Control'] = 'no-cache'
  return json.dumps(data)

@put('/products/<product>')
def update_product(product):
  """Handles product updates"""
  try: 
    body = request.body.read()
    data[product] = int(body)
    response.status = 200 # OK
  except KeyError:
    response.status = 400 # Conflict
  except Exception:
    response.status = 500 # Internal Server Error
  response.headers['Content-Type'] = 'application/json'
  return json.dumps(data)

@delete('/products/<product>')
def delete_product(product):
  """Handles product deletion"""
  try:
    if product not in data.keys():
      raise KeyError
    del data[product]
    response.status = 200 # OK
  except KeyError:
    response.status = 409 # Conflict
  except Exception:
    response.status = 500 # Internal Server Error
  response.headers['Content-Type'] = 'application/json'
  return json.dumps(data)



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

  parser.add_argument('-v', '--verbose',
                      dest='verbose',
                      help='Define the verbosity',
                      type=bool,
                      default=True)

  options = parser.parse_args()
  host = options.host
  port = options.port
  verbose = options.verbose

  run(host=host, port=port, debug=verbose)

if __name__ == '__main__':
  main()
