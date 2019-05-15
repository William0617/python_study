#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/13 下午7:49
# @Author : wlsun
# @Site : 
# @File : chat_client
# @Software: PyCharm

import socket

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print('connection is success')
info = ''
while info != 'byebye':
    send_data = input('input data:')
    s.send(send_data.encode())
    if info == 'byebye':
        break
    info = s.recv(1024).decode()
    print('the receive content: %s' % info)
s.close()