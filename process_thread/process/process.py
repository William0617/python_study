# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 12:33
# File: process.py
# IDE: PyCharm
import os
import time
from multiprocessing import Process


# 1. 使用Process子类创建进程


class SubProcess(Process):

    def __init__(self, interval, name=''):
        super(SubProcess, self).__init__()
        self.interval = interval
        if name:
            self.name = name

    def run(self):
        print('the child process:%s start... its parent is %s.' % (
        os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_end = time.time()
        print('the child process:%s execute %0.2f seconds...' % (
        os.getpid(), t_end - t_start))


def main():
    print('the main process start...')
    p1 = SubProcess(interval=1, name='test')
    p2 = SubProcess(interval=2)
    p1.start()
    p2.start()
    print('p1.is_alive:%s' %p1.is_alive())
    print('p2.is_alive:%s'%p2.is_alive())
    print('p1.id=%s'%p1.pid)
    print('p1.name=%s'%p1.name)
    print('p2.id=%s'%p2.pid)
    print('p2.name=%s'%p2.name)
    p1.join()
    p2.join()
    print('the main process end...')


if __name__ == '__main__':
    main()