#!/usr/bin/python

from ftplib import FTP
from threading import Thread,Lock
from Queue import Queue

ftplist = [ 'ftp5.fr.freebsd.org','ftp.int-evry.fr','ftp.fr.debian.org','twiska.zarb.org','ftp.oleane.net','ubuntu.univ-reims.fr','ftp.free.fr','mirrorservice.org','ftp.belnet.be','ftp.uni-koeln.de','ftp.ciril.fr' ]

class WorkerThread(Thread):

  def __init__(self,queue,lock):
    Thread.__init__(self)
    self.queue = queue
    self.lock= lock

  def run(self):
    while ftplist:
      ftpsrv = str(self.queue.get())
      print "### %s ###" % ftpsrv
      ftp = FTP(ftpsrv)
      ftp.login()
      rootlist = []
      ftp.retrlines('LIST', rootlist.append)
      ftp.quit()
      self.queue.task_done()
      self.lock.acquire()
      print 'lock acquired by %s' % self.name
      output = open('file.txt','a')
      for line in rootlist:
        output.write(line)
      output.close()
      print 'write done by %s' % self.name
      print 'lock released by %s' % self.name
      self.lock.release()

queue = Queue()
lock = Lock()

for i in range(5):
  print "Creating worker thread %d " % i
  worker = WorkerThread(queue,lock)
  worker.setDaemon(True)
  worker.start()
  print "Worker thread %d created" % i

for ftpsrv in ftplist:
  queue.put(ftpsrv)

queue.join()

print "Work is done"

