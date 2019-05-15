# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-04 16:34
# File: set.py
# IDE: PyCharm

# 3. 集合的差集，并集和交集运算
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
# 交集
print(set_a & set_b)
# 并集
print(set_a | set_b)
# 差集
print(set_a - set_b)

# 2. 集合的添加和删除
# 添加元素
set5 = {'双鱼座', '水瓶座', '射手座', '双子座'}
set5.add('狮子座')
# 删除元素三种方法
set5.remove('狮子座')  # 删除指定元素
set5.pop()  # 删除随机元素
set5.clear()  # 删除所有元素

# 1. 集合的创建
set1 = {'双鱼座', '水瓶座', '射手座', '双子座'}
print(set1)
set2 = {'双鱼座', '水瓶座', '射手座', '双子座', '水瓶座'}
print(set1)
# 空集合
set3 = set()
# 列表转集合
list1 = {'双鱼座', '水瓶座', '射手座', '双子座'}
set4 = set(list1)
print(set4)
