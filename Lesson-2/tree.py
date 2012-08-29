#!/usr/bin/python
import os, sys

walk = os.walk(sys.argv[1])
    
for i in sorted(walk):
    mydir = i[0]
    d = mydir.split("/")
    n = len(d)
    print '|' + '----'*n + ' /' + d[-1]
    
    for f in os.listdir(mydir):
        myfile =  mydir + '/' + f
        if os.path.isfile(myfile):
            print '|' + '----'*(n+1) + ' ' + f

