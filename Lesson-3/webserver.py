#!/usr/bin/python

import SocketServer
import SimpleHTTPServer

class myHttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/gruik':
			self.wfile.write('<h1>gruik gruik</h1>')
		else:
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

serveraddr = ('0.0.0.0',6667)
wwwserver = SocketServer.TCPServer(serveraddr,myHttpHandler)

wwwserver.serve_forever()
