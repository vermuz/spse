#!/usr/bin/python

class Calc:

  def __init__(self,num_a,num_b):
    self.num_a = num_a
    self.num_b = num_b

  def sub(self):
    return self.num_a - self.num_b

  def div(self):
    return self.num_a / self.num_b

  def add(self):
    return self.num_a + self.num_b

  def mul(self):
    return self.num_a * self.num_b

a = int(raw_input("Give a number: "))
b = int(raw_input("Give another number: "))

class SciCalc(Calc):

  def sub(self):
    return 10000

  def power(self): 
    return a**b 

Operation = SciCalc(a,b)

print "%d - %d = %d" % (a,b,Operation.sub())
print "%d ** %d = %d" % (a,b,Operation.power())

