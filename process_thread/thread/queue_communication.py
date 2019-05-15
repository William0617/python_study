# _*_ coding:utf-8 _*_
# Author: william.sun
# Time: 2019-05-12 15:43
# File: queue_communication.py
# IDE: PyCharm
import random
import time
from queue import Queue
from threading import Thread

# 使用队列模拟生产者消费者模式
class Producer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name = name)
        self.data = queue

    def run(self):
        for i in range(5):
            print('producer %s add product %d' % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.random())
        print('producer %s completed' % self.getName())

class Consumer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name = name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get(i)
            print('Consumer %s get product %d' % (self.getName(), val))
            time.sleep(random.random ())
        print('Consumer %s completed' % self.getName())

if __name__ == '__main__':
    print('main thread start===')
    q = Queue()
    producer = Producer('Producer', q)
    consumer = Consumer('Producer', q)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('main thread end===')
