# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 12:00
# File: mysql_02.py
# IDE: PyCharm

import pymysql
# 2. 创建表
# cursor.execute('drop table if exists books')
db = pymysql.connect(host='localhost', user='root', password='123456', database='test', charset='utf8')
cursor = db.cursor()
sql = """
CREATE TABLE books(
 id int(8) NOT NULL AUTO_INCREMENT,
 name varchar(50) NOT NULL,
 category varchar(50) NOT NULL,
 price decimal(10, 2) DEFAULT NULL,
 publish_time date DEFAULT NULL,
 PRIMARY KEY (id)
 ) ENGINE = MYISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
result = cursor.execute(sql)
print(result)
cursor.close()
db.close()