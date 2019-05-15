# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 15:06
# File: thread_creation01.py
# IDE: PyCharm

from threading import Thread
import time
# 使用thread子类创建线程

class SubThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = 'subthread' + self.name + ' execute' + str(i)
            print(msg)

if __name__ == '__main__':
    print('main thread start=====')
    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('main thread end=====')