#-*- coding:utf-8 -*-

import socket

'''
官方文档见：https://docs.python.org/3/library/socket.html 
中文博客：http://www.cnblogs.com/alan-babyblog/p/5260156.html
为了测试一下以下几种情况：
1、长字符串，超出recv的buffersize大小该怎么接收
2、短字符串，小于recv的buffersize的大小会怎么样
这里简单介绍一下可能用到的方法：
socket.getpeername() return the remote address to which the socket is connect
socket.getsockname() return the socket's own address
socket.recv(bufsize[,flags]) return a bytes object representing the data received
socket.recvfrom(bufsize[,flags]) return a pair (bytes,address)
socket.send(bytes[,flags]) return the number of bytes send
socket.sendall(bytes[,flags]) unlike send(), it continues to send data from bytes until either all data has
      been sent or an error occurs,return None if succeed or raise expections if failed
socket.sendto(bytes,flags,address)
'''

def socket_connect():
    addr = ('localhost',6379)
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.connect(addr)
    return c

def data_recv(length,c):
    data = ""
    while length > 0:
        if length > 1024:
            data = data + c.recv(1024).decode()
            length = length - 1024
        else:
            #之前忘了将recv（）参数改为length，导致错误
            data = data + c.recv(length).decode()
            length = length -1024
        
    return data

if __name__ == '__main__':
    c = socket_connect()
    
    data_bytes = c.recv(1024)
    data_str = data_bytes.decode()
    print(data_str,int(data_str[4:12]))
    data_recved = data_recv(int(data_str[4:12]),c)
    print(data_recved)
    