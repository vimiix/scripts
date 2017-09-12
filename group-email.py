#coding=utf-8
#
#**************************************
# 文件名:group email.py
# 功能：实现发邮件
# 作者：vimiix
#***************************************

import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import smtplib

#发件邮箱配置
sender = "nigelyq@163.com"  #"发件邮箱地址"
usrname= "nigelyq"          #"发件人"
passwd = "nigelyao"         #"发件邮箱密码"
host   = "smtp.163.com"     #"发件邮箱的smtp服务器"
port   = 25

#邮件正文
body   = "This is a test email from Vimiix :)"

#要群发的电子邮件地址，写在一个元祖中
recipients = ("i@vimiix.com",)

try:
    #登录电子邮箱服务器
    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(usrname, passwd)

    #开始群发
    for recipient in recipients:
        #创建邮件
        msg = MIMEMultipart()
        msg.set_charset("utf-8")
        msg.add_header("From", sender)
        msg.add_header("To", recipient)
        msg.add_header("Subject", "This is a test")
        msg.attach(MIMEText(body, "plain", _charset="utf-8"))

        #添加图片
        '''
        with open("test.jpg", "rb") as f:
            msg.attach(MIMEImage(f.read()))
        '''

        #添加附件邮件
        '''
        attachment = MIMEBase("text", "txt")
        with open("test.txt", "rb") as f:
            attachment.set_payload(f.read())
    
        email.encoders.encode_base64(attachment)
        attachment.add_header("content-disposition", "attachment",
                              filename=("utf-8", "test.txt"))
        msg.attach(attachment)
        '''

        #发送邮件
        try:
            server.sendmail(sender, recipient, msg.as_string(),)
            print("Send Success!")
        except smtplib.SMTPException:
            print("Error")
    server.quit()
except smtplib.SMTPException:
    print("Error")


