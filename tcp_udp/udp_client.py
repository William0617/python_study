#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/13 下午8:09
# @Author : wlsun
# @Site : 
# @File : udp_client
# @Software: PyCharm

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input('input: ')
s.sendto(data.encode(), ('127.0.0.1', 8888))
print('the result is: %s' % s.recv(1024).decode())
s.close()
