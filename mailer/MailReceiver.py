# coding: GB2312

import smtplib
import getpass, poplib
import email

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.Header import Header
from email.Header import decode_header
from types import *
import smtplib,poplib,string,sys,os,email

def prompt(prompt):
    return raw_input(prompt).strip()

smtpHost = 'smtp.163.com'
popHost = 'pop.163.com'

fromaddr = "superesb@163.com"
toaddrs  = ("wangerqi@supermap.com").split()

strMsg = "Just a test msg."
strUser = "superesb@163.com"
strPWD = "super527"

helptext = """
Available commands:
i     - index display
l n?  - list all messages (or just message n)
d n?  - mark all messages for deletion (or just message n)
s n?  - save input num messages to a file (or just message n)
m     - compose and send a new mail message
q     - quit pymail
?     - display this help text
"""

#简单的菜单处理,无返回值，要求一个处理过的mail列表
def interact(processmail):
    #showindex(processmail)
    while 1:
        try:
            command=raw_input('[Pymail] Action? (i, l, d, s, m, q, ?) ')
        except EOFError:
            command='q'

        if command=='q' or not command:
            break

        elif command[0]=='i':
            showindex(processmail)

        elif command[0]=='l':
            if len(command)==1:
                for mail in processmail:
                    showmessage(mail)
                    print string.join(message)
            else:
                if 0<msgnum(command)<=len(processmail):
                    num=msgnum(command)
                    showsubject(processmail[num-1])
                    showmessage(processmail[num-1])
        elif command[0]=='s':
            if len(command)==1:
                print '请输入要保存的邮件号码'
                continue
            else:
                if 0<msgnum(command)<=len(processmail):
                    num=msgnum(command)
                    savemail(processmail[num-1])

        elif command[0]=='?':
            print helptext

        else:
            print 'What? -- type "?" for commands help'

#保存email未完成           
def savemail(mail):
    filename=raw_input('Enter a file name:')
    #file=open('filename','w')
    #print >;>; file,showsubject(mail),showmessage(mail)
    print 'saving mail to %s ok.' %(filename)

#处理输入的数字   
def msgnum(command):
    try:
        return string.atoi(string.split(command)[1])
    except:
        return -1

def POPconnect():
    #sname,user,passwd=popconfig()
    server=poplib.POP3(popHost)
    server.user(strUser)
    server.pass_(strPWD)
    print server.getwelcome()
    return server

def loadmail():
    server=POPconnect()
    try:
        print server.list()
        (mailCount,mailByte)=server.stat()
        print 'There are',mailCount,'mail messages in',mailByte,'bytes'
        print 'Retrieving:'
        mailList=[]
        for i in range(mailCount):
            print i+1,
            (hdr,message,octet)=server.retr(i+1)
            mailList.append(string.join(message,'\n'))
        print
        assert len(mailList)==mailCount
        return mailList

    finally:
        server.quit()

#处理loadmain返回的原始mail列表，返回处理过的processmail列表
def processmail(mailList):
    processmaillist=[]
    for i in range(len(mailList)):
        processmaillist.append(email.message_from_string(mailList[i]))
    return processmaillist

def showsubjectall(mailList):
	for m in mailList:
		print showsubject(m)
		
#显示邮件主题，要求一个处理过的mail做参数
def showsubject(mail):
    header=[]
    for head in decode_header(mail.get('subject')):
        #if head[1]=='utf-8':
         #   header.append(unicode(head[0],'utf-8'))
        #else:
        #    header.append(head[0])

        if head[1]=='utf-8':
            header.append(unicode(head[0],'utf-8'))
        else:
            header.append(head[0])
            
    for sub in ('From','Date','Subject'):
        if sub=='Subject':
            print 'Subject:',
            for subject in header:
                try:
                    print subject,
                except UnicodeEncodeError:
                    print '注意:这个邮件标题无法正常显示...'
        else:
            print 'Unknown: %s:%s' %(sub,mail[sub])
    print      

def showmessageall(mailList):
	for m in mailList:
		print showmessage(m)
		print ""	
		print "============New Mail==============="	

def processAttach(par):
	#有附件
	# 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
	h = email.Header.Header(name)
	dh = email.Header.decode_header(h)
	fname = dh[0][0]

	#print '有附件'+fname
	data = par.get_payload(decode=True) #　解码出附件数据，然后存储到文件中
	atta[fname]=data
	try:
	    f = open(fname, 'wb') #注意一定要用wb来打开文件，因为附件一般都是二进制文件
	except:
	    print '附件名有非法字符，自动换一个'
	    f = open('aaaa', 'wb')
	f.write(data)
	f.close()

def processPart(mail):
	type=mail.get_content_charset()
	print "charset: ",type
	print ""
	
	if type==None:
		print mail.get_payload()
	elif type=='utf-8':
		try:
			#print unicode(mail.get_payload(decode='base64'),type)
			print unicode(mail.get_payload(),type)
		except UnicodeDecodeError,UnicodeEncodeError:
			print "Error Decode UTF-8: "
	else:
		#print mail.get_payload('base64')
		payLoad = mail.get_payload()
		contentTypes = payLoad['Content-Type']
		tranEncoding = payLoad['Content-Transfer-Encoding']
		attachName = payLoad.get_param("name")
		print contentTypes,'',tranEncoding,'',attachName

def processPart2(par):
	content_type=par.get_content_type()
	charset = par.get_charset()
	print "content_type:",content_type
	print "charset:",charset
	if content_type in ['text/plain']:
		if charset==None:
			textplain=par.get_payload(decode=True)
		else:
			textplain=par.get_payload(decode=True).decode(charset)
		print textplain
	if content_type in ['text/html']:
		if charset==None:
			#texthtml=par.get_payload(decode=True)
			texthtml=tryDecode(par.get_payload(decode=True))
		else:
			texthtml=par.get_payload(decode=True).decode(charset)
		
		try:
			print texthtml
		except UnicodeError:
			print "Uknown codec."

#尝试修复charset: None
def tryDecode(msg):
	#m = tryDecodeUnicode(msg)
	#if  m != "":
	#	return m
	m = tryDecodeGB2312(msg)
	if  m != "":
		return m
	m = tryDecodeGBK(msg)
	if  m != "":
		return m
	return "Try Decode fail."	
		
def tryDecodeUnicode(msg):
	try:
		print "tryDecodeUnicode"
		m = msg.decode('utf-8')
		return m
	except UnicodeError:
		return ""

def tryDecodeGB2312(msg):
	try:
		print "tryDecodeGB2312"
		m = msg.decode('gb2312')
		return m
	except UnicodeError:
		return ""

def tryDecodeGBK(msg):
	try:
		print "tryDecodeGBK"
		m = msg.decode('gbk')
		return m
	except UnicodeError:
		return ""

#显示邮件内容，要求一个处理过的mail做参数
def showmessage(mail):
	if mail.is_multipart():
		for part in mail.get_payload():
			showmessage(part)
	else:
		name = mail.get_param("name") #如果是附件，这里就会取出附件的文件名
		if name:
			print "is a attach."
		else:
			processPart2(mail)
	print ""	
	print "============New Part==============="	
		
			
#显示全部邮件主题要求整个处理过的邮件列表
def showindex(processmaillist):
    count=1
    for mail in processmaillist:
        print count,
        showsubject(mail)
        print 
        if count%5==0:
            raw_input("\n[Press Enter key]")
        count+=1

#输入发送时需要的服务器名等相关信息，返回一个元组
def sendconfig():
    SMTPname=raw_input('SMTPserverName?')
    SMTPuser=raw_input('SMTPusername?')
    SMTPpass=raw_input('SMTPServerPassword?')
    To=raw_input('To?')
    From=raw_input('From?')
    return SMTPname,SMTPuser,SMTPpass,to,From

#输入接收邮件时需要的相关输入，返回一个元组
def popconfig():
   POPname=raw_input('POPServerName?')
   POPuser=raw_input('POPusername?')
   POPpass=raw_input('POPpassword?')
   return POPname,POPuser,POPpass

if __name__=='__main__':
    list=loadmail()
    mailList=processmail(list)
    #showsubjectall(mailList)
    showmessageall(mailList)
    
    #interact(maillist)

#numMessages = len(M.list()[1])
#print "Msg Count:",numMessages
#for i in range(numMessages):
#    for j in M.retr(i+1)[1]:
#        print j
    #print M.retr(i+1)[1]

#M.quit()