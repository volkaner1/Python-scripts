#!/usr/bin/python2

import SimpleHTTPServer as server
import BaseHTTPServer

class ServerPutHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        server.SimpleHTTPRequestHandler.do_GET(self)

    def do_PUT(self):
        file_length=int(self.headers['Content-Length'])
        path=self.translate_path(self.path)
        with open(path,"wb") as output:
            output.write(self.rfile.read(file_length))

if __name__=='__main__':
    server.test(HandlerClass=ServerPutHTTPRequestHandler)
