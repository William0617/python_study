# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-02 15:38
# File: tuple.py
# IDE: PyCharm
import random

num = (7, 14, 21, 28, 35, 42)
str_tuple = ('渔舟唱晚', '高山流水', '出水莲', '汉宫秋月')
# 单元素元组
one = ('hahah',)

tuple1 = tuple(range(10, 20, 1))
# 索引输出
print(str_tuple[1])
# 切片输出
print(str_tuple[1:3:1])
# print函数输出
print(str_tuple)
# 两个元组可以通过加号连接
# 元组推导式
randomNum = (random.randint(10, 100) for i in range(10))
print(tuple(randomNum))
# print(randomNum.__next__())
# print(randomNum.__next__())
