import smtplibfrom email.mime.multipart 
import MIMEMultipartfrom email.mime.text 
import MIMETextfrom email.mime.image 
import MIMEImage

#����ʵ��,����MIMEMultipart������Ϊ������
msg=MIMEMultipart()
msg['Subject']='this is title'
msg['From']=mail_from
msg['To']=';'.join(mail_to) 

# ����MIMEText������Ϊ�ʼ���ʾ���ݲ����ӵ�������
txt=MIMEText(u'������������Ŷ','plain','utf-8')
msg.attach(txt) picfiles=['', '', ...]  
#ͼƬ·��
for file in picfiles: 
	f=open(file,'rb')
	img=MIMEImage(f.read())
	f.close()
	msg.attach(img) 
	smtp=smtplib.SMTP()
	smtp.connect('smtp.126.com')
	smtp.login('�û���','����')
	smtp.sendmail(mail_from,mail_to,msg.as_string()) 