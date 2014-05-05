#coding=utf-8
import datetime
import logging
import xlrd
import xlwt
import urllib
from xlutils.copy import copy
import os
import tempfile
import shutil
import MySQLdb
import sys
from contextlib import contextmanager
log = logging.getLogger(__name__)


# 字符集处理
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


# 连接数据库
conn = MySQLdb.connect(host='192.168.0.131',
                       db='tbkt',
                       user='dba_user',
                       passwd='tbkt123456',
                       charset="utf8")

net_ketang = MySQLdb.connect(host='192.168.0.131',
                       db='net_ketang',
                       user='dba_user',
                       passwd='tbkt123456',
                       charset="utf8")


cxn = conn.cursor()
net_cxn = net_ketang.cursor()
#文件服务器
FILE_WEB_URLROOT = 'http://file.tbkt.cn'

@contextmanager
def tempinput(file_):
    """
    功能说明：                 远程文件保存临时文件
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    方朋                    2014－04－28
    """
    temp = tempfile.NamedTemporaryFile(delete=False)
    shutil.copyfileobj(file_, temp)
    temp.close()
    yield temp.name
    os.unlink(temp.name)


def choiceFile():
    """
    功能说明：                 找未处理的数据
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    方朋                    2014－04－28
    """
    sql = """
        select * from class_import where status=0;
    """
    param = ['id', 'school_id', 'grade', 'school_type', 'learn_length', 'unit_class_id', 'user_id', 'subject', 'import_num', 'import_ok_num', 'add_date', 'status', 'file_path', 'file_name', 'file_size', 'send_open', 'send_user', 'add_user_name', 'school_name', 'county', 'class_id']
    files = SelectAllSqlByColumns(sql, param)
    if files:
        print u'共%s个Excel表格正在导入……' % len(files)
        if handle_file(files):
            print u'处理完成！'
        else:
            print u'处理失败！'

    else:
        print u'暂无数据'


def handle_file(files):
    """
    功能说明：                 处理数据批量导入数据
    -----------------------------------------------
    修改人                    修改时间
    -----------------------------------------------
    方朋                    2014－04－17
    """
    now = datetime.datetime.now()
    try:
        for f in files:
            # 更新数据库
            sql = """
                update class_import set status=%s where id = %s;
            """ % (1, f['id'])
            cxn.execute(sql)
            conn.commit()

            # 处理远程文件
            file_path = f['file_path']
            file_path = FILE_WEB_URLROOT+'/upload_media/'+file_path
            file_data = urllib.urlopen(file_path)

            # 调用获取班级学校信息存储过程
            get_class_info_parms = (
                f['school_id'],         # 学校ID
                f['school_type'],       # 学校类型
                f['learn_length'],      # 学制
                3,                      # 节点级别 班级为 3
                f['grade'],             # 年级 ID
                f['class_id']           # 班级id
            )
            class_info = callProc('get_school_unit_class', get_class_info_parms)
            if class_info:
                class_info = class_info[0]
                province = class_info[5] if class_info[5] else ""   # 学校所在省
                city = class_info[6] if class_info[6] else ""       # 学校所在城市

            # 读取远程文件
            with tempinput(file_data) as tempfilename:
                data = xlrd.open_workbook(tempfilename, formatting_info=True)
                sheets = data.sheets()
                all_num, ok_num = 0, 0                  # 总计数目/成功数目
                count = 0                               # 区表索引
                for obj in sheets:                      # 检索工作表
                    table = obj
                    nrows = table.nrows
                    ncols = table.ncols
                    # 遍历整行和列
                    for i in range(10, nrows):      # 从第10行开始
                        all_num += 1
                        rows = table.row_values(i)
                        # 格式如下：家长姓名/性别/学生姓名/与学生关系/手机号/确认码
                        sex = 1 if rows[1] == '男' else 2
                        try:
                            # 调用批处理存储过程
                            param = (
                                2,                  # 操作类型 1 暂存 2 开通账号 3 开通学科 4换班
                                str(int(rows[4])),            # 手机号
                                f['user_id'],       # 操作用户 ID
                                rows[2],            # 用户姓名
                                sex,                # 性别
                                1,                  # 用户类型 1 学生 3 教师
                                rows[3],            # 关系
                                int(f['send_user']),     # 是否下发账号密码 0 不下发 1 下发 2 已有账号不下发
                                1,                  # 批处理 ID 0 代表 非批处理操作
                                int(f['school_id']),            # 学校 ID
                                f['school_type'],                  # 学校类型
                                f['school_name'],       # 学校名称
                                province,               # 学校所在省
                                city,                   # 学校所在市
                                f['county'],            # 学校所在区县
                                f['grade'],             # 年级 ID
                                f['class_id'],          # 班级 ID
                                f['unit_class_id'],     # 班级表 ID
                                f['subject'],           # 开通学科
                                1,                      # 开通方式 1 确认码 2短信 3 试用 4 暂存
                                int(rows[5])            # 确认码
                            )
                            # 调用存储过程
                            result = callNetProc('batch_process', param)
                            errs = ""   # 错误原因
                            if result:
                                if result[0] != 1:
                                    ok_num += 1

                            # 创建class_import_detail数据
                            sql2 = """
                            insert into class_import_detail (classimport_id,parent_name,sex,username,relation,phone_number,identify_code,status,errms,add_time)
                            values(%s,'%s',%s,'%s','%s','%s',%s,%s,'%s','%s')
                            """ % (f['id'], rows[0], sex, rows[2], rows[3], int(rows[4]), int(rows[5]), 1, errs, now)
                            cxn.execute(sql2)
                            conn.commit()

                        except Exception, e:
                            print e
                            log.error('handle_file:%s' %e)

                    count += 1
                # 更新数据库
                sql3 = """
                    update class_import set import_num=%s,import_ok_num=%s,status=%s where id = %s;
                """ % (all_num, ok_num, 2, f['id'])
                cxn.execute(sql3)
                conn.commit()
                return True
            return False
    except Exception, e:
        log.error('handle_file:%s' %e)
        return False


def callProc(proname, args):
    """
    功能说明：                 调用存储过程
    -----------------------------------------------
    修改人                    修改时间
    cxn: 游标对象
    -----------------------------------------------
    方朋                    2014－04－28
    """
    try:
        _cxn = conn.cursor()
        format_s = '%s,'*(len(args)-1)
        format_s += '%s'
        st = 'call %s(%s)' % (proname, format_s)
        _cxn.execute(st, args)
        data = _cxn.fetchall()
        return data
    except Exception,e:
        log.info('callProc:%s' %e)
        return False


def callNetProc(proname, args):
    """
    功能说明：                 调用存储过程
    -----------------------------------------------
    修改人                    修改时间
    cxn: 游标对象
    -----------------------------------------------
    方朋                    2014－04－28
    """
    try:
        _cxn = net_ketang.cursor()
        format_s = '%s,'*(len(args)-1)
        format_s += '%s'
        st = 'call %s(%s)' % (proname, format_s)
        _cxn.execute(st, args)
        data = _cxn.fetchall()
        return data
    except Exception,e:
        log.info('callProc:%s' %e)
        return False


def SelectAllSqlByColumns(sql, columns):
    """
    功能说明：       SQL原始查询
    --------------------------------
    修改人        修改时间        修改原因
    --------------------------------
    """
    if sql is None or sql == "":
        return
    cxn.execute(sql)
    fetchall = cxn.fetchall()
    object_list = []
    if fetchall:
        for obj in fetchall:
            dict = {}
            for index, c in enumerate(columns):
                dict[c] = obj[index]
            object_list.append(dict)
    return object_list



def main():
    choiceFile()


if __name__ == '__main__':
    main()
    cxn.close()
    conn.close()
