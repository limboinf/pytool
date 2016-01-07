# coding=utf-8
#!/usr/bin/env python
# send_email.py - Send email
# Copyright (C) 2015 BeginMan. <xinxinyu2011@163.com>

__author__ = 'BeginMan'
import smtplib
import re
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


MAIL_HOST = 'smtp.exmail.qq.com'
MAIL_USER = '1373763906'
MAIL_PWD = '***********'
MAIL_POSTFIX = 'qq.com' # 发件箱的后缀


err_send_mails = os.path.join(os.path.dirname(__file__), 'err_send_mails.txt')
Template = os.path.join(os.path.dirname(__file__), 'template/')

def log_email():
    emails = os.path.join(os.path.dirname(__file__), 'emails.txt')
    if not os.path.isfile(emails):
        print u'没有找到邮箱文件'
        return None

    emails_list = []
    with open(emails) as f:
        for line in f.readlines():
            try:
                email = line.replace('\n', '')
                if check_email(email):
                    emails_list.append(email)
                else:
                    write_err_log(line)
            except:
                write_err_log(line)

    return emails_list



def write_err_log(err_email):
    """记录错误邮箱以及没有发送成功的邮箱"""
    with open(err_send_mails, 'a+') as err_file:
        if err_email.endswith('\n'):
            err_file.write(err_email)
        else:
            err_file.write(err_email+'\n')



def check_email(email):
    """检查邮件异常处理"""
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0




class SendMail(object):
    def __init__(self, host=MAIL_HOST, user=MAIL_USER, pwd=MAIL_PWD, postfix=MAIL_POSTFIX, mailto_list=None):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.postfix = postfix
        self.mailto_list = mailto_list      # 收件人列表



    def gen_msg(self,msgObj,sub):
        """创建并组织邮件头"""
        me="拨号精灵"+"<"+self.user+"@"+self.postfix+">"        # 头部显示
        msgObj['Subject'] = sub
        msgObj['From'] = me
        # msgObj['To'] = ";".join(self.mailto_list)             # 发送多个
        msgObj['To'] = self.mailto_list                         # 发送单个
        return msgObj


    def send_mail_server(self, msgObj):
        """发送邮件服务"""
        try:
            # server = smtplib.SMTP()
            # server.connect(self.host)

            # server = smtplib.SMTP_SSL(self.host, '465')
            # server.login(self.user, self.pwd)

            # 个人邮件服务器
            server = smtplib.SMTP('123.56.102.154')

            server.sendmail(msgObj['From'], self.mailto_list, msgObj.as_string())
            server.close()
            return True
        except Exception, e:
            write_err_log(self.mailto_list[0])
            print e
            return False

    def send_mail(self, sub, content, emial_type=1):
        """
        arg:
            sub: 邮件主题
            content: 邮件内容
            emial_type:默认1，邮件类型，1：文本；2.html
        :return
            True & False
        """
        _subtype ='plain' if emial_type == 1 else 'html'
        msgObj = MIMEText(content, _subtype=_subtype, _charset='utf-8')
        msgObj = self.gen_msg(msgObj, sub)
        return self.send_mail_server(msgObj)

    def send_mail_with_attachment(self, sub, file_datas):
        #发送带附件邮件
        msg = MIMEMultipart()       # 创建一个带附件的实例
        msg = self.gen_msg(msg, sub)

        def attachment(file_path, file_name):
            #构造附件1
            att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="%s"' % file_name #这里的filename可以任意写，写什么名字，邮件中显示什么名字
            msg.attach(att1)

        for k, v in file_datas.items():
            attachment(v, k)

        return self.send_mail_server(msg)



def send_muti_email():
    emails = log_email()
    with open(os.path.join(Template, 'template1.html')) as html:
        html = html.read()
        for index, obj in enumerate(emails):
            print u'正在向第%s位用户:%s 发送邮箱.....' % (index+1, obj)
            if SendMail(mailto_list=obj).send_mail("拨号精灵致老朋友的一封信！", html, emial_type=2):
                print u'发送成功！'
            else:
                print u'发送失败，已写入错误邮箱日志中!'

            time.sleep(1)


if __name__ == '__main__':
    # SendMail().send_mail("拨号精灵提示","测试项目！")
    # SendMail().send_mail("拨号精灵提示Html", "<h1>Hello</h1>", emial_type=2)
    # SendMail().send_mail_with_attachment("拨号精灵提示File", {
    #     'c.py':'/Users/fang/tmp/c.py',
    # })
    send_muti_email()
    #454 Authentication failed, please open smtp flag first!： 原因是我使用的QQ邮箱没有开通POP3/SMTP服务，登录邮箱开启该服务即可
    #ImportError: No module named email.utils: 项目名称不要用Python标准库起名，如原先项目名:email.这样与标准库email冲突了
