# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 14:59
# File: thread_creation.py
# IDE: PyCharm

# 1. threading模块的Thread类创建
import threading
import time

def thread():
    for i in range(3):
        time.sleep(1)
        print('thread name is %s' % threading.current_thread().name)

if __name__ == '__main__':
    print('main thread start=====')
    threads = [threading.Thread(target=thread) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('main thread end=====')
