#!/usr/bin/env python
from pybloomfilter import BloomFilter
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import os.path
import sys
import json

bloomFilePath = sys.argv[1]
bf = BloomFilter.open(bloomFilePath)


class BloomREST(BaseHTTPRequestHandler):
    def getValues(self):
        contentLength = int(self.headers['Content-Length'])
        postData = self.rfile.read(contentLength)
        values = json.loads(unicode(postData))
        return values

    def do_POST(self):
        if self.path == '/check':
            try:
                values = self.getValues()

                answer = []
                for value in values:
                    answer.append(value in bf)

                self.send_response(200)
                self.end_headers()
                self.wfile.write(unicode(json.dumps(answer)))
            except:
                self.send_response(400)
                self.end_headers()
                self.wfile.write('')

            return
        if self.path == '/add':
            try:
                values = self.getValues()

                bf.update(values)

                self.send_response(200)
            except:
                self.send_response(400)

            self.end_headers()
            self.wfile.write('')
            return


port = int(sys.argv[2])
SocketServer.TCPServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(('0.0.0.0', port), BloomREST)
httpd.serve_forever()
