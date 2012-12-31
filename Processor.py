#! /usr/bin/env python

import logging
from tornado.ioloop import IOLoop
from stormed import Connection, Message
import simplejson as json

def on_connect():
    ch = conn.channel()
    ch.queue_declare(queue='reply')
    ch.consume('reply', callback, no_ack=True)

def callback(msg):
	print " [x] Received %r" % msg.body
	runmsg(msg)
	
def runmsg(msg):
	print "Exec", msg.body
	strMsg = json.loads(msg.body)
	print "Head:",strMsg[0]
	print "Body:",strMsg[1]
	#exec msg
	
logging.basicConfig()
conn = Connection(host='localhost')
conn.connect(on_connect)
io_loop = IOLoop.instance()
print ' [*] Waiting for messages. To exit press CTRL+C'

try:
    io_loop.start()
except KeyboardInterrupt:
    conn.close(io_loop.stop)
