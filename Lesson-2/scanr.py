#!/usr/bin/python

from sys import argv
from threading import Thread
from Queue import Queue
from scapy.all import sr1,IP,TCP

dstip = argv[1]
ports = argv[2]
ports = ports.split('-')
prange = range(int(ports[0]),int(ports[1]))

print prange

class MyScanr(Thread):

	def __init__(self,queue):
		Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			port = self.queue.get()
			answer = sr1(IP(dst=dstip)/TCP(dport=port,flags='S'),timeout=1,verbose=0)
			if answer['TCP'].flags == 18:
				print "Port %s open" % port
			self.queue.task_done()

queue = Queue()

print "########### SCAN STARTED ###########"

for i in range(10):
	scanr = MyScanr(queue)
	scanr.setDaemon(True)
	scanr.start()

for port in prange:
	port = int(port)
	queue.put(port)

queue.join()

print "########## SCAN FINISHED ###########"
