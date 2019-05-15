# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-04 21:32
# File: inheritance.py
# IDE: PyCharm

# 6. 继承


class Fruit:
    color = 'green'

    def harvest(self, color):
        print('the fruit is:', color)
        print('the original color is:', Fruit.color)


class Apple(Fruit):
    color = 'red'

    def __init__(self):
        print('i am apple')


class Orange(Fruit):
    color = 'orange'

    def __init__(self):
        print('i am orange')


apple = Apple()
apple.harvest(apple.color)
orange = Orange()
apple.harvest(orange.color)
