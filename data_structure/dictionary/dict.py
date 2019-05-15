# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-04 15:40
# File: dict.py
# IDE: PyCharm
import random

# 6.

# 5. 字典推导式：{值表达式：键表达式 for}
random_dict = {i: random.randint(1, 10) for i in range(1, 10)}
print(random_dict)

# 4. 添加，修改和删除字典中的元素
dict6 = {'che': '车', 'chen': '尘', 'cheng': '惩', 'chi': '吃'}
dict6['ha'] = '哈'
del dict6['ha']
print(dict6)

# 3. 遍历字典: iterms()
dict5 = {'che': '车', 'chen': '尘', 'cheng': '惩', 'chi': '吃'}
for value in dict5.items():
    print(value)
for key, value in dict5.items():
    print(key, value)

# 2. 通过键值对访问字典：value = dict[key]
dict4 = {'che': '车', 'chen': '尘', 'cheng': '惩', 'chi': '吃'}
value = dict4.get('che','没有') # 第二个参数为默认值
print(value)

# 1. 创建字典
dict1 = {'che': '车', 'chen': '尘', 'cheng': '惩', 'chi': '吃'}
print(dict1)
# 两个列表组成一个dictionary，dict(zip（）)
list1 = ['che', 'chen', 'cheng', 'chi']
list2 = ['车', '尘', '称', '吃']
zip1 = dict(zip(list1, list2))
print(zip1)
# 通过一个元组和一个列表创建dictionary
tuple1 = ('che', 'chen', 'cheng', 'chi')
list3 = ['车', '尘', '称', '吃']
dict2 = {tuple1: list3}
print(dict2)
# 创建只有名字的字典fromkeys()
dict3 = dict.fromkeys(list3)
# 删除字典:del dict
# 删除字典中所有元素：dict.clear()

