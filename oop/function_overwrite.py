# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-04 21:32
# File: inheritance.py
# IDE: PyCharm

# 7. 方法重写
# 8. 子类调用父类构造方法


class Fruit:
    def __init__(self, color='green'):
        Fruit.color = color

    def harvest(self, color):
        print('the fruit is:', color)
        print('the original color is:', Fruit.color)


class Apple(Fruit):
    color = 'red'

    def __init__(self):
        print('i am apple')
        super().__init__()  # 子类调用父类构造方法

    def harvest(self, color):
        print('the apple is:', color)
        print('the apple original color is:', Fruit.color)


class Orange(Fruit):
    color = 'orange'

    def __init__(self):
        print('i am orange')
        super().__init__()  # 子类调用父类构造方法

    def harvest(self, color):
        print('the orange is:', color)
        print('the orange original color is:', Fruit.color)


class Renshenguo(Fruit):

    def __init__(self, color):
        print('i am renshenguo')
        super().__init__(color)

    def harvest(self, color):
        print('the renshenguo is:', color)
        print('the renshenguo original color is:', Fruit.color)


renshenguo = Renshenguo('white')
renshenguo.harvest('gold')
apple = Apple()
apple.harvest(apple.color)
orange = Orange()
apple.harvest(orange.color)
