# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 14:07
# File: communication.py
# IDE: PyCharm

# 进程间的通信-无法通信的例子
from multiprocessing import Process

g_num = 100

def plus():
    print('process 1 start===')
    global g_num
    g_num += 50
    print('g_num=%d'%g_num)
    print('process 1 end===')


def minus():
    print('process 2 start===')
    global g_num
    g_num -= 50
    print('g_num=%d' % g_num)
    print('process 2 end===')


if __name__ == '__main__':
    print('main process start====')
    p1 = Process(target=plus)
    p2 = Process(target=minus)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('main process end====')