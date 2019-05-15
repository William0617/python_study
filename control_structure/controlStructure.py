# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-04 14:06
# File: controlStructure.py
# IDE: PyCharm

# 3. while loop
flag = True
num = 0
while flag:
	num += 1
	if 5 == num:
		flag = False
	print(num, end=" ")

# 2. for statement
# range([start], end, [step])
for i in range(10):
	print(i,  end=" ")
for i in "哈哈哈哈或":
	print(i, end=" ")

# 1. if statement
i = 5
if i > 7:
	print('')
else:
	print('')



