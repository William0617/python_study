# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-02 14:48
# File: list.py
# IDE: PyCharm
import random

number = [2, 4, 6, 8, 10]
verse = ['春眠不觉晓', '处处闻啼鸟', '夜来风雨声', '花落知多少']
py = ['优雅', "明确", '''简单''']
untitile = ['python', 29, 'haha']
empty = []
num = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print(py[0:3:1])
a = list(range(2, 21, 2))
print(a)
# 列表推导式
list_a = []
# for i in range(10):
#     list_a.append(random.randint(10, 100))
# print(list_a)
list_b = [random.randint(10, 100) for i in range(10)]
price = [10, 20, 30, 40, 50]
list_c = [int(x * 0.5) for x in price]
list_d = [x for x in price if x > 20]
# 列表统计，统计某元素出现次数
print(a.count(1))
# 计算某元素出现的位置
print(a.index(10))
# 常用统计函数
print(max(num))
print(min(num))
print(len(num))
print(sum(num))
# 排序
num.sort()  # list.sort()功能是针对列表自己内部进行排序， 不会有返回值， 因此返回为None。
print(num)
print(list(sorted(num)))  # 不改变原来的内容
# 追加元素
a.append('add element')
print(a)
# 插入元素
a.insert(2, 'haha') # 效率不如append，不推荐
print(a)
# 追加其他列表
a.extend(verse)
print(a)
# 删除元素
del verse[2]
print(verse)
# 修改元素
verse[2] = 'hahhahhh'
print(verse)
# 根据值删除元素
# a.remove('2')
# print(a)


















