# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 13:59
# File: process02.py
# IDE: PyCharm

from multiprocessing import Pool
import os
import time

# 3. 使用进程池创建进程

def task(name):
    print('child process %s execute task %s'%(os.getpid(), name))
    time.sleep(1)

if __name__ == '__main__':
    print('parent(%s)'%os.getpid())
    p = Pool(3)
    for i in range(10):
        p.apply_async(task, args=(i,))
    p.close()
    p.join()
    print('all children end')
