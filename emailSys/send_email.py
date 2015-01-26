# coding=utf-8
__author__ = 'fang'
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


MAIL_HOST = 'smtp.exmail.qq.com'
MAIL_USER = '1373763906'
MAIL_PWD = '***********'
MAIL_POSTFIX = 'qq.com' # 发件箱的后缀

mailto_list = ['xinxinyu2011@163.com']


class SendMail(object):
    def __init__(self, host=MAIL_HOST, user=MAIL_USER, pwd=MAIL_PWD, postfix=MAIL_POSTFIX, mailto_list=mailto_list):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.postfix = postfix
        self.mailto_list = mailto_list      # 收件人列表

    def check_email(self):
        """检查邮件异常处理"""
        #TODO


    def gen_msg(self,msgObj,sub):
        """创建并组织邮件头"""
        me="拨号精灵"+"<"+self.user+"@"+self.postfix+">"        # 头部显示
        msgObj['Subject'] = sub
        msgObj['From'] = me
        msgObj['To'] = ";".join(self.mailto_list)
        return msgObj


    def send_mail_server(self, msgObj):
        """发送邮件服务"""
        try:
            server = smtplib.SMTP()
            server.connect(self.host)
            server.login(self.user, self.pwd)
            server.sendmail(msgObj['From'], self.mailto_list, msgObj.as_string())
            server.close()
            return True
        except Exception, e:
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



if __name__ == '__main__':
    # SendMail().send_mail("拨号精灵提示","测试项目！")
    SendMail().send_mail("拨号精灵提示Html", "<h1>Hello</h1>", emial_type=2)
    # SendMail().send_mail_with_attachment("拨号精灵提示File", {
    #     'c.py':'/Users/fang/tmp/c.py',
    # })

    pass

#Reference:http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html
#454 Authentication failed, please open smtp flag first!： 原因是我使用的QQ邮箱没有开通POP3/SMTP服务，登录邮箱开启该服务即可
#ImportError: No module named email.utils: 项目名称不要用Python标准库起名，如原先项目名:email.这样与标准库email冲突了

#My blog:http://www.cnblogs.com/BeginMan/p/3443158.html
