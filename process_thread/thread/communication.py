# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 15:17
# File: communication.py
# IDE: PyCharm

from threading import Thread

g_num = 100

def plus():
    print('thread 1 start===')
    global g_num
    g_num += 50
    print('g_num=%d'%g_num)
    print('thread 1 end===')


def minus():
    print('thread 2 start===')
    global g_num
    g_num -= 50
    print('g_num=%d' % g_num)
    print('thread 2 end===')


if __name__ == '__main__':
    print('main thread start====')
    # q = Queue()
    t1 = Thread(target=plus)
    t2 = Thread(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('main thread end=====')