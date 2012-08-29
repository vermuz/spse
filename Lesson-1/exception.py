#!/usr/bin/python

class myError(Exception):
  def __init__(self,value):
    self.value = value
  def __str__(self):
    return repr(self.value)

def divide(a,b):
  if b != 0:
    return a / b
  else:
    raise myError("Can't divide by zero")

try:
  print str(divide(4,2))
  print str(divide(2,0))
except myError, error:
   print error
