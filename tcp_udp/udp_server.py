#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/13 下午8:05
# @Author : wlsun
# @Site : 
# @File : udp_server
# @Software: PyCharm

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))
data, addr = s.recvfrom(1024) # receivefrom() return a tuple
data = float(data) * 1.8 + 32
send_data = 'the result is :' + str(data)
print('received from %s : %s' % addr)
s.sendto(send_data.encode(), addr)
s.close()