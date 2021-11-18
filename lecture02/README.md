# Simple Mail Transfer Protocol
[<img src="https://img.shields.io/badge/os-linux%20%7C%20macOS%20%7C%20windows-green">](os|Linux-macOS)
[<img src="https://img.shields.io/badge/python-v3-blue">](python|v3)

In this lecture, I’ll provide a walkthrough of how to build a SMTP client using smtplib, a Python standard library.

## SMTP Overview
SMTP was originally specified in [RFC 821](https://datatracker.ietf.org/doc/html/rfc821) and then revised in [RFC 5321](https://datatracker.ietf.org/doc/html/rfc5321). It sends emails with a connection-oriented approach and notifies the status of delivery and errors.

The SMTP architecture is normally composed of two subsystems: user agents and message transfer agent. A **user agent** is a program that provides a graphical or textual interface for interacting with the e-mail system. It includes tools to compose, reply to, view and organize messages. **Message transfer agents** are typically system processes. They run as services on mail servers and are meant to be always available. Their job is to automatically move emails through the source system to the recipient using SMTP. **Mailboxes** are the link between user agent and message transfer agent. They store e-mails received by users within the mail servers, and let user agents present them to end-users.

The messages consist of header fields, a blank line and the body of the message. It is possible to send ASCII and non-ASCII characters, the latter through the Multipurpos Internet Mail Extension (MIME).

## References
- [Sending Emails With Python](https://realpython.com/python-send-email/#yagmail)
- [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml)
