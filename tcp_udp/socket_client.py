#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/13 下午4:39
# @Author : wlsun
# @Site : 
# @File : socket_creation
# @Software: PyCharm

import socket

host = '127.0.0.1'
port = 8080
client = socket.socket()
client.connect((host, port))
send_data = input('Please input:')
client.send(send_data.encode())
recv_data = client.recv(1024).decode()
print('The data is %s' % recv_data)
client.close()

