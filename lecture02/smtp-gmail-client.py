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
__description__ = 'SMTP Gmail Client'


import ssl
import argparse
from smtplib import SMTP_SSL
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

    parser.add_argument('-s', '--sender',
                        dest='sender_email',
                        help='Define the sender',
                        type=str,
                        required=True)

    parser.add_argument('-r', '--receiver',
                        dest='receiver_email',
                        help='Define the receiver',
                        type=str,
                        required=True)

    options = parser.parse_args()
    verbose = options.verbose
    sender_email = options.sender_email
    receiver_email = options.receiver_email
    host = "smtp.gmail.com"
    port = 465
    password = input("Type your password and press enter: ")
    text = """
        Hey there,

        This email is sent out from a Python SMTP Client.
        Cool, right?!
    """
    message = MIMEText(text, "plain")
    message["Subject"] = "Hi there from Python SMTP Client!"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    context = ssl.create_default_context()
    with SMTP_SSL(host, port, context=context) as client:
        client.set_debuglevel(verbose)
        client.login(sender_email, password)
        client.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == '__main__':
    main()