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

import SMUP
import SMUP_Image

#=================================================================
global handle_Dispatcher

def on_connect():
	global str_Status
	global str_Jobs
	global ch_Status
	global ch_Jobs
	global isMonitor
	
	str_Jobs = 'com.supermap.smpp.jobs'
	str_Status = 'com.supermap.smpp.status'
	
	#建立任务分发通道
	ch_Jobs = conn.channel()
	ch_Jobs.queue_declare(queue=str_Jobs)	
	
	#建立任务状态接收通道
	ch_Status = conn.channel()
	ch_Status.exchange_declare(exchange=str_Status,type='fanout')	
	
	isMonitor = False
	if isMonitor == True:
		ch_Status.queue_declare(exclusive=True,callback=with_status_queue)	

	#派发任务
	handle_Dispatcher(ch_Jobs)

def Start():
	global conn
	global io_loop

	logging.basicConfig()
	conn = Connection(host='localhost')
	conn.connect(on_connect)
	io_loop = IOLoop.instance()
	io_loop.start()

def close():
	conn.close(callback=done)
	
def done():
	print " End."
	io_loop.stop()
	
def with_status_queue(qinfo):
	ch_Status.queue_bind(exchange=str_Status,queue=qinfo.queue)
	ch_Status.consume(qinfo.queue, on_status, no_ack=True)

def on_status(msg):
	print "Status: %r" % msg.body

def sendStatus(strStatusInfo):
	'Send status to Monitor on another queue.'
	strReport = ["status","status info."]
	strReport[1] = strStatusInfo
	strReport_json = json.dumps(strReport)
	msgReport = Message(strReport_json)
	ch_Status.publish(msgReport, exchange=str_Status, routing_key='')
	return strReport_json

def send_job(job):
	ch_Jobs.publish(job, exchange='', routing_key=str_Jobs)
	
def dispatch_jobs(ch):
	print "Dispatch Job:"
	
if __name__ == '__main__':
	handle_Dispatcher = dispatch_jobs
	Start()
