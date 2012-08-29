#!/usr/bin/python

from ftplib import FTP
from threading import Thread
from Queue import Queue

ftplist = [ 'ftp5.fr.freebsd.org','ftp.int-evry.fr','ftp.fr.debian.org','twiska.zarb.org','ftp.oleane.net','ubuntu.univ-reims.fr','ftp.free.fr','mirrorservice.org','ftp.belnet.be','ftp.uni-koeln.de','ftp.ciril.fr' ]

class WorkerThread(Thread):

  def __init__(self,queue):
    Thread.__init__(self)
    self.queue = queue

  def run(self):
    while True:
      ftpsrv = str(self.queue.get())
      print "### %s ###" % ftpsrv
      ftp = FTP(ftpsrv)
      ftp.login()
      ftp.retrlines('LIST')
      ftp.quit()
      self.queue.task_done()

queue = Queue()

for i in range(5):
  print "Creating worker thread %d " % i
  worker = WorkerThread(queue)
  worker.setDaemon(True)
  worker.start()
  print "Worker thread %d created" % i

for ftpsrv in ftplist:
  queue.put(ftpsrv)

queue.join()

print "Work is done"

