#coding=utf-8
import logging
import datetime
import time
import MySQLdb
from django.db import connections, connection,transaction
log = logging.getLogger(__name__)

def ExecuteSql(sql):
    """
    功能说明：   执行SQL
    --------------------------------
    修改人        修改时间        修改原因
    --------------------------------
    方朋        2014-01-06
    """
    if sql is None or sql == "":
        return

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    return True


def SelectAllSql(sql):
    """
    功能说明：       查询SQL多条数据
    --------------------------------
    修改人        修改时间        修改原因
    --------------------------------
    方朋        2014-01-06
    """
    if sql is None or sql == "":
        return
    cursor = connection.cursor()
    cursor.execute(sql)
    fetchall = cursor.fetchall()
    cursor.close()
    return fetchall


def SelectAllSqlByColumns(sql,columns):
    """
    功能说明：       查询SQL多条数据
    --------------------------------
    修改人        修改时间        修改原因
    --------------------------------
    陈龙       2014-04-11
    参数示例：
    sql = "select username ,password from user"
    columns= ["username","password"]
  returns:
        [
        {"username":"陈龙","password":"密码"},
        {"username":"徐威","password":"密码"}
        ]
    """
    if sql is None or sql == "":
        return
    cursor = connection.cursor()
    cursor.execute(sql)
    fetchall = cursor.fetchall()
    object_list = []
    if fetchall:
        for obj in fetchall:
            dict = {}
            for index,c in enumerate(columns):
                dict[c] = obj[index]
            object_list.append(dict)
    cursor.close()
    return object_list

def SelectOneSql(sql):
    """
    功能说明：       查询SQL单条数据
    --------------------------------
    修改人        修改时间        修改原因
    --------------------------------
    方朋        2014-01-06
    """
    if sql is None or sql == "":
        return
    cursor = connection.cursor()
    cursor.execute(sql)
    fetchone = cursor.fetchone()
    cursor.close()
    return fetchone


def SelectOneSqlByColumns(sql,columns):
    """
    功能说明：       查询SQL单条数据
    --------------------------------
    修改人        修改时间        修改原因
    --------------------------------
    陈龙       2014-04-11
    参数示例：
    sql = "select username ,password from user"
    columns= ["username","password"]
    
  returns:{"username":"陈龙","password":"密码"},
        
    """
    if sql is None or sql == "":
        return
    cursor = connection.cursor()
    cursor.execute(sql)
    fetchone = cursor.fetchone()
    object = {}
    if fetchone:
        for index, c in enumerate(columns):
            object[c] = fetchone[index]
    cursor.close()
    return object

def callProc(proname, params):
    """
    功能说明：                调用存储过程
    -----------------------------------------------
    修改人                   修改时间
    -----------------------------------------------
    方朋                    2014－04－17
    proname:    存储过程名字
    params:     输入参数元组或列表
    """
    cc = connections['ketang'].cursor()
    db = 'ketang'
    if proname == 'get_school_unit_class':      # 获取班级学校信息的存储过程在tbkt里面。
        cc = connection.cursor()
        db = 'default'
    try:
        cc.callproc(proname, params)
        print u'该存储[%s]过程影响的行数：%s' % (proname, cc.rowcount)
        try:
            transaction.commit_unless_managed(using=db)     # 事务提交
        except Exception, e:
            pass

        data = cc.fetchall()
        print '存储过程返回的数据：%s' %data
        cc.close()
        return data

    except Exception, e:
        log.info('callProc:%s' % e)
        return 'err'
    finally:
        cc.close()


def SelectRawSqlByColumns(cxn, sql, columns):
    """
    功能说明：       SQL原始查询
    --------------------------------
    修改人        修改时间        修改原因
    --------------------------------
    方朋           2014/04/28
    cxn: 游标对象
    sql: 原始SQL语句
    """

    if not isinstance(cxn, MySQLdb.cursors.Cursor):
        return False

    if sql is None or sql == "":
        return False

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