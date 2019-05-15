#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/13 下午7:30
# @Author : wlsun
# @Site : 
# @File : socket_server
# @Software: PyCharm

import socket
# create tcp server
host = '127.0.0.1'
port = 8080

web = socket.socket()
web.bind((host, port))
web.listen(5)
print('Server is waiting for connection:')
while True:
    conn, addr = web.accept()  # conn是新的socket对象；addr是客户端的ip
    data = conn.recv(1024)
    print(data)
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello World')
    conn.close()
    web.close()
