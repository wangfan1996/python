import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr

my_sender = '15732638907@163.com'  # 发件人邮箱账号
my_pass = 'wangfan1996'  # 发件人邮箱密码

my_user = ['1356316925@qq.com', ]  # 收件人邮箱账号

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""

msg = MIMEMultipart()
msg['From'] = formataddr(["我叫王帆", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
msg['Subject'] = "学习python发送邮件测试"  # 邮件的主题，也可以说是标题

msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('test.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
server.quit()  # 关闭连接
print("邮件发送成功")
