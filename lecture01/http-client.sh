#!/bin/bash
# This is a HTTP client in Bash
#
# Copyright 2021, FCRlab at University of Messina
# Lorenzo Carnevale <lcarnevale@unime.it>
#
# Remember to start the HTTP server first
# You are also invited to run the curl from the command line

echo ">> create two new products"
curl -X POST http://localhost:8080/products \
    -d '{"pizza": 1, "water": 6}' \
    -H "Content-Type: application/json" \
    -i
echo ""

echo ">> create an existing product"
curl -X POST http://localhost:8080/products \
    -d '{"water": 6}' \
    -H "Content-Type: application/json" \
    -i
echo ""

echo ">> list all products"
curl -X GET http://localhost:8080/products \
    -i
echo ""

echo ">> update a product"
curl -X PUT http://localhost:8080/products/pizza \
    -d '2' \
    -H "Content-Type: text/plain" \
    -i
echo ""

echo ">> delete a product"
curl -X DELETE http://localhost:8080/products/water \
    -i
echo ""

echo ">> list all products"
curl -X GET http://localhost:8080/products \
    -i
echo ""

exit 0