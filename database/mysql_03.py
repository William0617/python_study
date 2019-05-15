# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 12:00
# File: mysql_03.py
# IDE: PyCharm

import pymysql

# 3. 操作表CURD

# 1) INSERT
db = pymysql.connect(host='localhost', user='root', password='123456', database='test', charset='utf8')
cursor = db.cursor()

data = ('introduction to python', 'python', '50.20', '2019-02-05')
data1 = [('introduction to python', 'python', '50.20', '2019-02-05'),
            ('introduction to python', 'python', '50.20', '2019-02-05'),
            ('introduction to python', 'python', '50.20', '2019-02-05'),
         ]
sql = """
    INSERT INTO books(name, category, price, publish_time) 
        values(%s, %s, %s, %s)
"""
cursor.execute(sql, data)
cursor.executemany(sql,data1)
cursor.close()
db.close()

# 2)