# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-04 20:12
# File: oop.py
# IDE: PyCharm


class TV_show1:  # 5.2 为属性添加安全保护机制，使私有属性不能修改也不能被读取。使用property装饰器
    list_film = ['战狼', '红海行动', '西游记', '熊出没']

    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        return self.__show

    @show.setter
    def show(self, value):
        if value in TV_show1.list_film:
            self.__show = '您选择了' + value + '稍后将播放'
        else:
            self.__show = '您点播的电影不存在'


tv_show = TV_show1('战狼')
print('default output:', tv_show.show)  # 此时show为只读属性。不能被修改。
tv_show.show = '红海行动'  # 修改成功


class TV_show:  # 5.1 为属性添加安全保护机制，使私有属性不能修改也不能被读取。使用property装饰器

    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        return self.__show


tv_show = TV_show('playing zhanlang2')
print('default output:', tv_show.show)  # 此时show为只读属性。不能被修改。

# 4. 创建用于计算的属性。
# @property（装饰器）：把一个方法转化为属性。好处是可以通过方法名访问方法，不需要小括号。


class Rect:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rect(800, 600)
print('Area is:', rect.area)
# rect.area = 100  # 报错。不能直接赋值


class Swan:  # 3. 访问控制：属性或方法名前添加单下划线或者双下划线；系统方法在属性名或方法前后都添加双下划线
    # 1. _foo单下划线表示protected的成员：类本身和子类可以访问
    _neck = 'long'
    # 2. __bar双下划线表示private的成员：只有类本身可以访问
    __leg = 'thin'

    def __init__(self):
        print('__init__', Swan._neck)  # 访问protected类型的属性
        print('__init__', Swan.__leg)  # 访问private类型的属性

    def my(self):
        print('my function:', Swan.__leg)


swan = Swan()
print('通过实例名直接访问受保护类型的属性：' + swan._neck)
# print('通过实例名直接访问私有类型的属性：' + swan.__leg)  # 报错
print('修改私有类型的属性：' + swan._Swan__leg)  # 可以访问
swan._Swan__leg = 'long'  # 修改私有类型属性
print('通过实例名直接访问受保护类型的属性：' + swan._Swan__leg)  # 可以访问，只发生在类的定义时，不能改变方法中私有属性的值。所以是安全的。
swan.my()


class Geese1: # 2. 实例属性
    def __init__(self):
        # 实例属性
        self.neck = 'long'
        self.wing = 'great'
        self.leg = 'in the center of body'
        print(self.neck)
        print(self.wing)
        print(self.leg)


wild_geese = Geese1()


class Geese:  # 1. 类属性
    # 类属性
    neck = 'long'
    wing = 'great'
    leg = 'in the center of body'
    number = 0

    def __init__(self):
        Geese.number += 1
        print("this is geese class, # %d" % Geese.number)
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)

    def fly(self, state = 'I can fly'):
        print(state)


# wild_geese = Geese()
# wild_geese1 = Geese()
list1 = []
for i in range(1, 5):
    list1.append(Geese())
Geese.beak = 'high'
print(list1[2].beak)