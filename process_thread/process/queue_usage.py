# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 14:15
# File: queue_usage.py
# IDE: PyCharm

# 多进程队列的使用
from multiprocessing import Queue

if __name__ == '__main__':
    q = Queue(3)
    q.put('message 1')
    q.put('message 2')
    print('is the queue is full?', q.full())
    q.put('message 3')
    print('is the queue is full?', q.full())
    # print(q.qsize()) 在macOS无法使用
    if not q.empty():
        print('get message from queue---')
        while not q.empty():
            print(q.get_nowait())

    # try:
    #     q.put('message 4', True, 2)
    # except:
    #     print('the queue is full,there are %s message' % q.qsize())


