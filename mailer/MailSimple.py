import smtplibfrom email.mime.text
import MIMEText 

#正文
mail_body='hello, this is the mail content'

#发信邮箱
mail_from='sender@example.com'

#收信邮箱
mail_to=['to@example.com']

#定义正文
msg=MIMEText(mail_body)

#定义标题
msg['Subject']='this is the title'

#定义发信人
msg['From']=mail_from
msg['To']=';'.join(mail_to)

#定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z') 
smtp=smtplib.SMTP()

#连接SMTP服务器，此处用的126的SMTP服务器
smtp.connect('smtp.126.com')

#用户名密码smtp.login('用户名','密码')
smtp.sendmail(mail_from,mail_to,msg.as_string())
smtp.quit() 
print 'ok'
