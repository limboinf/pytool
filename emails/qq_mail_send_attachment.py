# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import os
import zipfile
import tempfile
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = '1373763906@qq.com'
receivers = ["xinxinyu2011@163.com", "1565208411@qq.com"]

# 第三方 SMTP 服务
mail_host="smtp.qq.com"    # 设置服务器
mail_user=sender
mail_pass="****"          # 口令


def send_mail():
    email_msg = MIMEMultipart()
    email_msg['Subject'] = Header("方朋发来的邮件", 'utf-8')
    email_msg['To'] = Header(', '.join(receivers), 'utf-8')
    email_msg['Form'] = Header(sender, 'utf-8')
    email_msg.preamble = "Hello, world!\n"      # 序文

    msg = MIMEBase('application', 'zip')
    msg.set_payload(zip_it().read())
    encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment', filename=os.getcwd()[-1] + '.zip')

    # 邮件正文内容
    email_msg.attach(msg)
    email_msg = email_msg.as_string()

    # send the message
    print "Sending email message..."
    try:
        smtp = smtplib.SMTP_SSL('smtp.qq.com')
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(sender, receivers, email_msg)
        print "邮件发送成功!"
    except smtplib.SMTPException, e:
        print "邮件发送失败," , e


def zip_it():
    zf = tempfile.TemporaryFile(prefix='test', suffix='.zip')
    zip_f = zipfile.ZipFile(zf, 'w')
    print "Zipping current dir: %s" % os.getcwd()
    for file_name in os.listdir(os.getcwd()):
        zip_f.write(file_name)

    zip_f.close()
    zf.seek(0)
    return zf


if __name__ == '__main__':
    send_mail()