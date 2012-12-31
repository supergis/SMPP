import smtplibfrom email.mime.multipart 
import MIMEMultipartfrom email.mime.text 
import MIMETextfrom email.mime.image 
import MIMEImage

#创建实例,构造MIMEMultipart对象做为根容器
msg=MIMEMultipart()
msg['Subject']='this is title'
msg['From']=mail_from
msg['To']=';'.join(mail_to) 

# 构造MIMEText对象做为邮件显示内容并附加到根容器
txt=MIMEText(u'这是中文内容哦','plain','utf-8')
msg.attach(txt) picfiles=['', '', ...]  
#图片路径
for file in picfiles: 
	f=open(file,'rb')
	img=MIMEImage(f.read())
	f.close()
	msg.attach(img) 
	smtp=smtplib.SMTP()
	smtp.connect('smtp.126.com')
	smtp.login('用户名','密码')
	smtp.sendmail(mail_from,mail_to,msg.as_string()) 