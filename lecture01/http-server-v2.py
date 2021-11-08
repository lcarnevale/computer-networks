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

import logging
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer

class SampleServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """Handler for the GET requests
        """
        logging.info('GET request, path %s, headers %s' % (str(self.path), str(self.headers)))

        self._set_response()
        message = ("GET request for %s" % (self.path)).encode('utf-8')
        self.wfile.write(message)

    def do_POST(self):
        """Handler for the POST requests
        """
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


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

    options = parser.parse_args()
    host = options.host
    port = options.port
    server_class=HTTPServer
    handler_class=SampleServer

    logging.basicConfig(level=logging.INFO)
    server_address = (host, port)
    httpd = HTTPServer(server_address, handler_class)
    logging.info('Starting httpd ...')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    logging.info('Stopping httpd ...')

if __name__ == '__main__':
    main()