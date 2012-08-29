#!/usr/bin/python

from scapy.all import *

response = sr1(IP(dst='192.168.1.254')/TCP(dport=80,flags='S'),verbose=0)

for i in response:
  print i.flags
