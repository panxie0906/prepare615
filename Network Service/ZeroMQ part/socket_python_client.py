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

#测试了一个客户端的情况：服务器多次往客户端发送数据，实际上是发送到缓冲区中去，客户端每次从缓冲区recv bufsize长度的数据
'''
还有一下情况没有测试：
1.如果服务器向多个客户端发送data，所用的缓冲区是一个吗？
2.如果多个客户端向服务器发送data，所用的缓冲区是同一个吗？
3.如果发送速度很快，导致缓冲区长度不够了怎么办？在看文档的过程中看到了阻塞和非阻塞形式的发送，可以考虑试一试
'''

def socket_connect():
    addr = ('localhost',6379)
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.connect(addr)
    return c

def data_recv(length,c):
    data = ""
    while length > 0:
        if length > 3072:
            #不知道是什么错误，有可能是recv（）到了数据末端？对socket的机制还是有点不那么熟悉
            #看到一句话
            #出现错误的原因是因为utf8格式一般是'\xef', '\xbb', '\xbf'三个一起出现，然后解析的，而在某处不能够成三个一组的时候就会出现这样的错误
            #果然如此，将1024换成3072即可
            data_tmp = c.recv(3072).decode()
            data = data + data_tmp
            length = length - 3072
        else:
            #之前忘了将recv（）参数改为length，导致错误 unexpected end of data
            data_tmp = c.recv(length).decode()
            data = data + data_tmp
            length = length -3072
        
    return data

if __name__ == '__main__':
    c = socket_connect()
    
    while True:
        try:
            data_bytes = c.recv(3072)
            data_str = data_bytes.decode()
            if data_str[0:4].isdigit():
                data_recved = data_recv(int(data_str[4:12]),c)
                print(data_recved)
            else:
                print('error')
        except EOFError:
            print('EOFError')