#!/usr/bin/python
# -*- encoding: utf-8 -*-

import BaseHTTPServer
import SimpleHTTPServer
import ssl
import os
import argparse
import sys
import signal

def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.abspath('.'), relative)

def stop_handler(signal, frame):
	httpd.socket.close()
	print 'The server was stopped'
	sys.exit()

#parse args
parser = argparse.ArgumentParser()
parser.add_argument('--https', action='store_true', help='Init https server')
parser.add_argument('-p', '--port', help='Set the port', type=int, default=3443)
parser.add_argument('-r', '--root', help='Set the root directory', default=os.getcwd())
args = parser.parse_args()

#go to the root directory
if not os.path.isdir(args.root):
    print '%s is not a directory' % args.root
    sys.exit()
os.chdir(args.root)

#create server
httpd = BaseHTTPServer.HTTPServer(
	('localhost', args.port), 
	SimpleHTTPServer.SimpleHTTPRequestHandler
)

#wrap socket for https mode
certfilepath = resource_path(os.path.join('data', 'cert.pem'))
if args.https:
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfilepath, server_side=True)

#register the signal(sigint) handler
signal.signal(signal.SIGINT, stop_handler)
signal.signal(signal.SIGTERM, stop_handler)

#print config
print 'The server is running now...'
print '    port: %d' % args.port
print '    mode: https' if args.https else '    mode: http'
print '    root: %s' % args.root
print 
print 'Press Ctrl+C to shutdown'

#start server
httpd.serve_forever()
