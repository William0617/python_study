# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 14:44
# File: use_queue_communication.py
# IDE: PyCharm

# 使用队列进行进程间通信

from multiprocessing import Queue, Process
import time


def write_task(q):
    count = 0
    while not q.full():
        if count <= 5:
            message = 'message'+ str(count)
            count += 1
            q.put(message)
            print('write %s'%message)


def read_task(q):
    time.sleep(1)
    while not q.empty():
        print('read:%s' % q.get(True, 2))


if __name__ == '__main__':
    print('main process start====')
    q = Queue()
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('main process end=====')
