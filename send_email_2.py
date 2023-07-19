#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

my_from='1127771903@qq.com'#发送方
password='atnobqgamdenfjch'#授权码
to=['1127771903@qq.com']#接收方，可以多个接收方，类似于群发


subject='测试邮件发送'   #主题
text='接口自动化测试报告'    #正文



msgRoot = MIMEMultipart('related')
massage=MIMEText(text)     #邮件对象
massage['Subject'] = subject   #给邮件添加主题
massage['From'] = my_from   #谁发送的
massage['To'] = ";".join(to)    #发给你想发送的对象

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('1.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)
    smtpObj.sendmail(my_from,to,massage.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
