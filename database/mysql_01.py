# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 10:30
# File: mysql_01.py
# IDE: PyCharm

import pymysql
# 1. 连接对象
# 流程： 创建connection连接对象->获取cursor->执行sql语句，处理执行结果->关闭cursor->关闭connection
db = pymysql.connect(host='localhost', user='root', password='123456', database='test', charset='utf8')
cursor = db.cursor()
cursor.execute('select version()')
result = cursor.fetchone()
print(result)
cursor.close()
db.close()





















