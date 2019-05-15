# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-07 22:23
# File: file.py
# IDE: PyCharm

# 5. 读取文件
# 5.1 读取指定字符
with open('status1.txt', 'r') as file5:
    # file5.seek(4)
    string = file5.read(4)
print(string)
# 5.2 读取一行
with open('status1.txt', 'r') as file6:
    line = file6.readline()
print(line)
# 5.3 读取所有行
with open('status1.txt', 'r') as file7:
    line1 = file7.readlines()
print(line1)

# 4. 写入文件内容
with open('status.txt', 'w') as file3:
    file3.write('111')
file4 = open('status.txt', 'a')

file4.write('aaaaa')
file4.flush()
file4.close()

# 3. 打开文件时使用with语句
with open('status1.txt', 'r', encoding='utf-8') as file:  # 创建文件
    pass
print(file.closed)  # 判断是否关闭

# 2. 关闭文件
file2 = open('status1.txt', 'r', encoding='utf-8')   # 创建文件
file2.close()
print(file2.closed)  # 判断是否关闭

# 1. 基本文件操作
# 1.1 创建和打开文件
file = open('status.txt', 'r', )   # 打开文件
file1 = open('status1.txt', 'r', encoding='utf-8')   # 创建文件
print(file1.read())

