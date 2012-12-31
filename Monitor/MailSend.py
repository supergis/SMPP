import smtplib

def prompt(prompt):
    return raw_input(prompt).strip()

mailHost = 'smtp.139.com'
fromaddr = "13901165523@139.com"
toaddrs  = ("wangerqi@supermap.com").split()
strMsg = "Just a test msg."
print "Send Messages.", mailHost, ", ", strMsg

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
msg = msg + strMsg

print "Message length is " + repr(len(msg))
print msg

server = smtplib.SMTP(mailHost)
server.set_debuglevel(2)

server.login("13901165523@139.com","super527")
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
