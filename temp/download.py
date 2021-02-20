#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import os
import pymysql
import requests
import json
import xlwt, re

'''
封装查询单条、多条数据
'''
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
pdbinfo = {"host": '172.16.112.26',
           "port": 3306,
           "user": 'root',
           "passwd": 'wangfan123',
           "db": 'mediumhardchain',
           "charset": 'utf8'}


class MySQLUtil:
    def __init__(self):
        self.dbinfo = pdbinfo
        self.conn = MySQLUtil.__getConnect(self.dbinfo)
        self.info_list = []
        self.dict_all = {}
        self.f_fail = open('/opt/提取失败日志.log', 'a', encoding='utf-8')

    @staticmethod
    def __getConnect(pdbinfo):
        try:
            conn = pymysql.connect(host=pdbinfo['host'], port=pdbinfo['port'], user=pdbinfo['user'],
                                   passwd=pdbinfo['passwd'],
                                   db=pdbinfo['db'], charset=pdbinfo['charset'])
            return conn
        except Exception as error:
            print("get connect happen error %s " % error)

    def close_db(self):
        try:
            self.conn.close()
        except Exception as error:
            print("close db happen error %s " % error)

    def get_alldata(self, psql):
        cur = self.conn.cursor()
        try:
            cur.execute(psql)
        except Exception as error:
            print("execute sql happen error %s " % error)
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    def get_singledata(self, psql):
        rows = self.get_alldata(psql)
        row_len = len(rows)
        print(row_len)

        if rows != None:
            for row in rows:
                for i in row:
                    print(i)
                    return i

    def update_loadstatus(self, ids):
        '''
        请求FDN2.0接口 实时 获取下载状态 & 下载状态描述
        更新数据库两个字段
        :return:
        '''
        print("000:", ids)
        print("===========查询FDN2.0接口===========")
        url = 'http://60.205.1.103:30200/guttv/fdn/orderwatch'
        headers = {'Content-Type': 'application/json'}
        id = "gzxmt_iptv|23010032020122121375933797"
        # data = {
        #     "task_id": id
        # }
        data = "[\r\n\t{\"task_id\": {}\r\n]".format(id)
        print("111:",data)   # 111: {'task_id': 'gzxmt_iptv|23010032020122121375933797'}
        print("222:",list(data)) # ['task_id']
        par = json.dumps(list(dict(data)))
        print("par:",par)   # ['task_id']
        res = requests.post(url, data=data, headers=headers)
        print("testinfo:", res)
        if res.content:
            rep = json.loads(res.content)[0]
            print("rep:", rep)
        else:
            print("==================")

    def action(self):
        selectSql = "select taskid from Distribution_mediadistribute where status = 50 or 1 "
        rows = self.get_alldata(selectSql)
        MySQLUtil().close_db()
        self.f_fail.close()
        print("rows:", rows)
        for i in rows:
            print("i:", i)
            print("查询数据：", i[0])
            self.update_loadstatus(i[0])


if __name__ == '__main__':
    conn = MySQLUtil().action()
