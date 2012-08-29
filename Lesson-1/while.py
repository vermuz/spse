#!/usr/bin/python

age = 33

while age > 10:
  age = int(raw_input("What is your age ? "))
  if age > 10:
    print "Your age is > %s" % age
    continue
  else:
    print "%s is too young" % age
