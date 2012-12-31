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
	global str_Status
	global str_Jobs
	global ch_Status
	global ch_Jobs

	str_Jobs = 'com.supermap.smpp.jobs'
	str_Status = 'com.supermap.smpp.status'
	
	ch_Status = conn.channel()
	ch_Status.exchange_declare(exchange=str_Status,type='fanout')
	
	ch_Jobs = conn.channel()
	#ch_Jobs.queue_declare(queue=str_Jobs)	
	ch_Jobs.queue_declare(queue=str_Jobs,durable=True)	
	ch_Jobs.qos(prefetch_count=1)
	ch_Jobs.consume(str_Jobs, on_job, no_ack=False)

def on_job(msg):
	'Main Worker, Process the job.'
	print "Received Job: %r" % msg.body
	strJob = json.loads(msg.body)
	if strJob[0]=="job":
		sendStatus(strJob[1])		
		handle_Processor(strJob[1])
	else:
		print "That's not My Job:"
		print "Head:",strJob[0]
		print "Body:",strJob[1]
	msg.ack()
	
def setProcessor(do_job):
	handle_Processor = do_job
	
def sendStatus(strStatusInfo):
	'Send status to Monitor on another queue.'
	strReport = ["status","status info."]
	strReport[1] = strStatusInfo
	strReport_json = json.dumps(strReport)
	msgReport = Message(strReport_json)
	ch_Status.publish(msgReport, exchange=str_Status, routing_key='')
	return strReport_json

def sendStatus_Test(ch):
	for i in range(1,10):
		msgTest = 'Status: STest at %02d' % i
		print "SendStatus Test:", sendStatus(msgTest)
		time.sleep(1)
		
def do_job(job):
	print "Do Job:", job
	sendStatus("Job Begin: %r"%job)
	time.sleep(5)
	sendStatus("Job Finish: %r"%job)

def done():
	print " End."
	io_loop.stop()

def Start():
	global conn
	global io_loop

	logging.basicConfig()
	conn = Connection(host='localhost')
	conn.connect(on_connect)
	io_loop = IOLoop.instance()
	io_loop.start()

global handle_Processor

if __name__ == '__main__':
	handle_Processor=do_job
	Start()
