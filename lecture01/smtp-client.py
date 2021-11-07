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

import argparse
from smtplib import SMTP as Client


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
                        default=8025)

    parser.add_argument('-s', '--sender',
                        dest='sender',
                        help='Define the sender',
                        type=str,
                        required=True)

    parser.add_argument('-r', '--receiver',
                        dest='receiver',
                        help='Define the receiver',
                        type=str,
                        required=True)

    options = parser.parse_args()
    host = options.host
    port = options.port
    sender = options.sender
    receiver = options.receiver

    client = Client(host, port)
    r = client.sendmail(sender, [receiver], """\
        From: Anne Person <anne@example.com>
        To: Bart Person <bart@example.com>
        Subject: A test
        Message-ID: <ant>

        Hi Bart, this is Anne.
    """)

if __name__ == '__main__':
    main()
