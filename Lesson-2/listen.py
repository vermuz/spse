#!/usr/bin/python

import signal
from socket import *
myHost = '127.0.0.1'
myPort = 666

s = socket(AF_INET, SOCK_STREAM)
s.bind((myHost, myPort))
s.listen(100)

def handler(signum,stack):
	print "Time to go to bed ..."

signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

while 1:
        connection, address = s.accept()
        while 1:
            data = connection.recv(1024)
            if data:
                connection.send('echo -> ' + data)
            else:
                break
        connection.close() 

