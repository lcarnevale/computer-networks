# Hypertext Transfer Protocol
[<img src="https://img.shields.io/badge/os-linux%20%7C%20macOS-green">](os|Linux-macOS)
[<img src="https://img.shields.io/badge/python-v3-blue">](python|v3)

In this lecture, I’ll provide a walkthrough of how to build a HTTP client-server model using Bottle, Requests and cURL.

You'll create CRUD APIs for creating, reading, update and delete products within a shopping list.

<center>

| Method | Pathname            | Body Type  |
|--------|---------------------|------------|
| POST   | /products           | JSON       |
| GET    | /products           |            |
| PUT    | /products/{product} | Plain Text |
| DELETE | /products/{product} |            |

</center>

## HTTP Overview
The Hypertext Transfer Protocol (HTTP) is a web's application-layer protocol that implements the client-server model:
- the client requests, receives and "displays" web objects, and
- the server sends objects in response to requests.

A HTTP client initiates a TCP connection (creates socket) to server, over the port 80. The server accepts the TCP connection from client. The hosts exchange HTTP messages before to close the TCP connection.

## Install Requirements
Create a virtual environment and install requirements as follow:
```bash
sudo pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## References
- [Bottle: Python Web Framework](https://bottlepy.org/docs/dev/index.html)
- [List of HTTP Status Code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
