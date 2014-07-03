#coding=utf-8
import logging
import simplejson as json
from django.db import connection
log = logging.getLogger(__name__)


def get_page(sql, columns, count_sql, page_no, page_num, url):
    """
    功能说明：     获取分页（获取当前页数据,和页面属性）
    --------------------------------
    修改人        修改时间        修改原因
    --------------------------------
    方朋        2014-04-16
    说明：
    ======================================================
    sql         —— 所有数据 sql 语句
    columns     —— 页面数据属性名,与 sql 的查询结果一一对应
    count_sql   —— 数据总数 sql 语句
    page_no     —— 页码
    page_num    —— 每页数据量
    url         —— 当前请求的 url (request.path)
    =======================================================
    返回数据：
    =======================================================
    {
        "object_lis":[],        —— 页面数据
        "page_attr":[1,65,""]   ——页面属性[页码,总页数,url]
    }
    =======================================================
    """

    if sql is None or sql == "":
        return
    try:
        cursor = connection.cursor()
        if isinstance(count_sql, int):
            count = count_sql
        else:
            cursor.execute(count_sql)
            count = cursor.fetchall()[0][0]     # 数据总数
        pages = (count/page_num)+1 if count % page_num < page_num else 0    # 总页数
        # 页面数据
        sql += """ limit %s,%s""" % ((int(page_no)-1)*page_num, page_num)
        cursor.execute(sql)
        fetchall = cursor.fetchall()
        object_lis = []        # 页面数据
        if fetchall:
            for obj in fetchall:
                dict = {}
                for index, c in enumerate(columns):
                    dict[c] = obj[index]
                object_lis.append(dict)
        return {
            'object_lis': object_lis,
            'page_attr': json.dumps([page_no, pages, url])
            }

    except Exception, e:
        log.info("get_page:%s" %e)
        return None









