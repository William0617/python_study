# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-04 11:50
# File: operation.py
# IDE: PyCharm

# 8. 格式化字符串
# (1)使用%操作符：：'%[-][+][0][m][.n]格式化字符串'%exp
template = '编号：%09d\t公司名称：%s\t官网：http://www.%s.com'
item = (7, '百度', 'baidu')
print(template%item)
# (2)使用format（）：template.format(args)

# 7. 去除字符串中空格等特殊字符：\t \n \r
# strip()
str11 = ' ' + '相信自 己' + ' '
print(str11.strip(' '))
# lstrip(): 去除左侧的空格等
# rstrip(): 去除右侧的空格等

# 6. 字母的大小写转换
# lower()
str_a = 'WWW.BAIDU.COM'
print(str_a.lower())
# upper()
str_b = 'www.baidu.com'
print(str_b.upper())

# 5. 检索字符串
# count()
str6 = 'i am a stupid student.'
print(str6.count('a'))
# find()
print(str6.find('st'))
print(str6.find('z'))
var = 'i' in str6
# index()
print(str6.index('a'))
print(str6.rindex('a'))
# startwith(), endswith()
print(str6.startswith('i'))
print(str6.endswith('.'))

# 4. 分割和合并字符串
# 分割字符串
str6 = 'i am a stupid student.'
print(str6.split(' ', -1))
print(str6.split(' ', 2))
# 合并字符串
str7 = ' @'
list8 = ['Jone', 'Tom', 'Bob']
print(str7.join(list8))

# 3. 截取字符串
str5 = 'i am a stupid student.'
print(str5[2:10:1])

# 2. 计算字符串长度
str4 = '汉字'
print(len(str4.encode()))
print(len(str4.encode('gbk')))

# 1. 拼接字符串，注意不能用加号把字符串和int型拼接
str1 = 'hello'
str2 = 'world'
print(str1 + ' ' + str2)
str3 = '\n'
print(str2 + str3 + str1)
