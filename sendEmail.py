import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


#确定发送方、邮箱授权码和接收方，邮件主题和内容
my_from='1127771903@qq.com'#发送方
password='atnobqgamdenfjch'#授权码
to=['1127771903@qq.com']#接收方，可以多个接收方，类似于群发


subject='测试邮件发送'   #主题
text='接口自动化测试报告'    #正文


#  邮件内容设置
# MIMEApplication用于发送各种文件，比如压缩，word，excel，pdf等


#这一部分是用于发送图片的代码
imageFile = r"1.jpg"
imageApart = MIMEImage(open(imageFile, 'rb').read())
imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
massage = MIMEMultipart()
massage.attach(imageApart)

# 构造邮件
massage.attach(MIMEText(text,'html'))


massage=MIMEText(text)     #邮件对象
massage['Subject'] = subject   #给邮件添加主题
massage['From'] = my_from   #谁发送的

massage['To'] = ";".join(to)    #发给你想发送的对象


#发送邮件，smtp.qq.com是qq邮箱的服务器地址（SMTP地址），465是他的端口号
s=smtplib.SMTP_SSL('smtp.qq.com',465)


#登录
s.login(my_from,password)


#发送方地址，接收方地址，邮件内容
#massage.as_string()会将邮件原封不动的发送
s.sendmail(my_from,to,massage.as_string())



