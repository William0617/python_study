#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/13 下午7:48
# @Author : wlsun
# @Site : 
# @File : chat_server
# @Software: PyCharm

import socket

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
sock, addr = s.accept()
print('the connection is success')
info = sock.recv(1024).decode()
while info != 'byebye':
    if info:
        print('the receive content: %s' %info)
    send_data = input('input the sending content:')
    sock.send(send_data.encode())
    if send_data == 'byebye':
        break
    info = sock.recv(1024).decode()
sock.close()
s.close()

