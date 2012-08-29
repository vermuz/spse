#!/usr/bin/python

import os

def child_proc():
    print "I'm the child process, my pid is %d" % os.getpid()
    print "The child is exiting"

def parent_proc():
    print "I'm the parent process, my pid is %d" % os.getpid()
    childpid = os.fork()
    if childpid == 0:
        child_proc()
    else:
        print "We are inside the parent process"
        print "Our child has the pid : %d" % childpid
   
    while True:
        pass

parent_proc()

