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
__description__ = 'SMTP Client'


import ssl
import argparse
from smtplib import SMTP
from email.mime.text import MIMEText


def main():
    description = ('%s\n%s' % (__author__, __description__))
    epilog = ('%s\n%s' % (__credits__, __copyright__))
    parser = argparse.ArgumentParser(
        description = description,
        epilog = epilog
    )

    parser.add_argument('-v', '--verbose',
                        dest='verbose',
                        help='Define the verbosity',
                        type=bool,
                        default=True)

    parser.add_argument('-H', '--host',
                        dest='host',
                        help='Define the host',
                        type=str,
                        default='localhost')
    
    parser.add_argument('-P', '--port',
                        dest='port',
                        help='Define the port',
                        type=int,
                        default=1025)

    options = parser.parse_args()
    verbose = options.verbose
    host = options.host
    port = options.port
    sender_email = "sender@email.com"
    receiver_email = "receiver@email.com"
    text = "Hey there,\nThis email is sent out from a Python SMTP Client."
    message = MIMEText(text, "plain")
    message["Subject"] = "Hi there from Python SMTP Client!"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    context = ssl.create_default_context()
    with SMTP(host, port) as client:
        client.set_debuglevel(verbose)
        client.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == '__main__':
    main()