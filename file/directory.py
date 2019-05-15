# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-08 21:55
# File: directory.py
# IDE: PyCharm

# 1. os和os.path模块
import os
import shutil

print(os.name)
print(os.linesep)
print(os.sep)

# 2. 路径
print(os.getcwd())
print(os.path.abspath(r'./file.py'))

# 3. 判断目录是否存在
print(os.path.exists('/Users/william.sun/PycharmProjects/python_study/dir'))

# 4. 创建目录
if not os.path.exists('./demo'):
    os.mkdir(r'./demo')
else:
    print('the dir is exited')
# 创建多层目录
os.makedirs(r'./demo1/demo2/demo3')

# 5. 删除目录
# os.rmdir('./demo')
shutil.rmtree('./demo1')

# 6. 遍历目录
for root, dirs, files in os.walk('./', topdown=True):
    print(root, dirs, files, '\n')

# 7. 删除文件
with open('./demo1.txt', 'w') as f:
    pass
os.remove('./demo1.txt')

# 8. 重命名文件或目录
if not os.path.exists('./demo.txt'):
    with open(r'./demo.txt', 'w') as f:
        pass
os.rename(r'./demo.txt', r'./test.txt')

# 9. 获取文件基本信息
print(os.stat('./file.py').st_ctime)
print(os.stat('./file.py').st_size)
print(os.stat('./file.py').st_mode)