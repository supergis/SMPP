# coding: GB2312
#!/usr/bin/env python
#SMUP-Parallel,SuperMap Universal Processor Parallel
# File: SMUPP.py
# Author: WangEQ, SuperMap GIS Institute.
# Desc: 

import math
import time
import sys

import logging
from tornado.ioloop import IOLoop
from stormed import Connection, Message
import simplejson as json

#=================================================================
def on_connect():
	global chOut
	chOut = conn.channel()
	chOut.queue_declare(queue='hello')	
	#SendHello(chOut)
	SendNo(chOut)

	global chIn
	chIn = conn.channel()
	chIn.queue_declare(queue='reply')	
	chOut.consume('reply', callback, no_ack=True)

def callback(msg):
	print " [x] Received %r" % msg.body
	strMsg = json.loads(msg.body)
	if strMsg[0]=="hello":
		SendReply(msg)
	else:
		print "Head:",strMsg[0]
		print "Body:",strMsg[1]
		
def SendHello(ch):
	strHello = ["hello","others"]
	strHello = json.dumps(strHello)
	print strHello
	
	msg = Message(strHello)
	ch.publish(msg, exchange='', routing_key='hello')
	print "Send Hello: ",msg.body

def SendNo(ch):
	for i in range(1,10):
		strHello = ["hello","others"]
		strHello[1] = 'Hello SMB %(ID)02d'%{"ID":i}
		msgno = Message( json.dumps(strHello) )
		ch.publish(msgno, exchange='', routing_key='hello')
		print "Send No ",i,"Finish"
		#time.sleep(1)
		
def done():
	print " End."
	io_loop.stop()

def SMBStart():
	global conn
	global io_loop
	logging.basicConfig()
	conn = Connection(host='localhost')
	conn.connect(on_connect)
	io_loop = IOLoop.instance()
	io_loop.start()

SMBStart()
