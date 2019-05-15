# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 15:29
# File: mutex.py
# IDE: PyCharm
import time
from threading import Thread, Lock
# 使用互斥锁
n = 100

def task():
    global  n
    mutex.acquire()
    time.sleep(0.1)
    n -= 1
    print('SUCCESS, there are %d tickets.'% n)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(10):
        t = Thread(target=task)
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()

