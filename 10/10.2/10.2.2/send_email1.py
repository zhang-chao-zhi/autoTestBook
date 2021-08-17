#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
#发送邮箱
sender = 'abc@163.com'
#接收邮箱
receiver = '123456@qq.com'
#发送邮件主题
subject = 'python email test'
#发送邮箱服务器
smtpserver = 'smtp.163.com'
#发送邮箱用户/密码
username = 'abc@163.com'
password = 'xxxxxxxx'
#中文需参数‘utf-8’，单字节字符不需要
msg = MIMEText('你好!','text','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()