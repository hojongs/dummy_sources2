#!/usr/bin/python

# echo client
from socket import *

host = 'localhost'
port = 6666

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host,port))
sock.send(str(1234))
buf = sock.recv(1024)
sock.close()
print buf
