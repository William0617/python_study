# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-02 11:50
# File: bmi.py
# IDE: PyCharm

height = float(input('Please input your height(meter):'))
weight = float(input('Please input your weight(kg):'))

bmi = weight / (height * height)
if bmi < 18.5:
    print('you are too thin')
elif 18.5 <= bmi < 24.9:
    print('Great')
elif 24.9 <= bmi < 29.9:
    print('heavy')
elif bmi >= 29.9:
    print('fat')
# print(id(bmi)) 查看内存地址
