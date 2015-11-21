#!/usr/bin/python

# echo server
from socket import *

host = ''
port = 6666

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind((host,port))
sock.listen(1)
conn,addr = sock.accept() #conn=sock, addr=(host,port)
print addr
buf=""
while not buf:
    buf = conn.recv(1024)
    conn.send(buf)
conn.close()
print buf

