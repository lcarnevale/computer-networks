#!/bin/bash
# This is a SMTP server in Bash
#
# Copyright 2021, FCRlab at University of Messina
# Lorenzo Carnevale <lcarnevale@unime.it>

echo "running SMTP server over localhost:1025"
python -m smtpd -c DebuggingServer -n localhost:1025