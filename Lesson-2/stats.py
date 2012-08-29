#/usr/bin/python
import os, sys

myfile = sys.argv[1]

for i in os.stat(myfile):
    print i

#print dir(os.stat(myfile))
