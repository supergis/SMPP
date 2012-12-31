#! /usr/bin/env python

import logging
from tornado.ioloop import IOLoop
from stormed import Connection, Message

def on_connect():
	global ch
	ch = conn.channel()
	ch.queue_declare(queue='hello')
	ch.consume('hello', callback, no_ack=True)

def callback(msg):
	print " [x] Received %r" % msg.body
	#msg.
	runMsg(msg.body)
	#msgR = Message("I am Zebra")
	#sendMsg(msgR)
	#runMsg("print 3")
	
def runMsg(msgExec):
	print "Exec",msgExec
	exec msgExec

def sendMsg(msg):
	ch.publish(msg, exchange='', routing_key='hello')

logging.basicConfig()
conn = Connection(host='localhost')
conn.connect(on_connect)
io_loop = IOLoop.instance()
print ' [*] Waiting for messages. To exit press CTRL+C'

try:
    io_loop.start()
except KeyboardInterrupt:
    conn.close(io_loop.stop)
