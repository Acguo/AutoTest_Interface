# -*- coding: UTF-8 -*-
import pymysql
import config
from pylog import Pylog

class DataBase:
    def __init__(self):
        self.host = config.get_config("database", "host")
        self.port = int(config.get_config("database", "port"))
        self.user = config.get_config("database", "user")
        self.pwd = config.get_config("database", "pwd")

    def get_connect(self,db):
        try:
            Pylog.info("开始连接数据库...")
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.pwd,db=db)
            cur = conn.cursor()
            return [cur,conn]
        except Exception as err:
            Pylog.error('mysql连接错误：' + str(err))

    #查询操作
    def inquire_data(self, sql, db):
        datas = []
        acon = self.get_connect(db)
        cur = acon[0]
        conn = acon[1]
        try:
            # 执行SQL语句
            cur.execute(sql)
            # 获取所有记录列表
            results = cur.fetchall()
            for row in results:
                datas.append(str(row[0]))
            cur.close()
            conn.close()
            Pylog.info("关闭数据库连接...")
            return datas
        except Exception as e:
            Pylog.error("查询错误 " + str(e))


if __name__ == "__main__":
    base = DataBase()
    ss = base.inquire_data("SELECT * FROM cms_check", "cms")
    print(ss)