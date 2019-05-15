# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-04 17:26
# File: function.py
# IDE: PyCharm

# 2. 函数参数
# *param 可变参数，所有参数转化为一个元组
# **param 可变参数，所有参数转化为一个字典

# 1. 函数的创建和调用


def filter_char(string):
    import re
    pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'
    sub = re.sub(pattern, '@_@', string)
    print(sub)


def empty():
    pass


filter_char("我是一名程序员，喜欢看黑客类的图书，正在研究Trojan")
filter_char("我是一名黑客，喜欢看黑客类的图书，正在研究Trojan")
