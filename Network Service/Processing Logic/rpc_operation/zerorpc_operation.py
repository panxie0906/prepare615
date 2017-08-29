# -*- coding:utf-8 -*-

'''
rpc俗称远程过程调用，也就是把本地的函数放在远端去调用
也就是说，被调用的具体实现不在程序运行本地，而是在别的某个地方（分布到各个服务器）
在615当中，xml解析和生成服务就可以写在主控端，而各个服务节点直接调用就可以了
基于http的rpc有两种xml-rpc和json-rpc，也就是基于http传输协议，xml或者json消息格式编码方式
具体实现代码见： http://developer.51cto.com/art/201407/446192.htm 
这里利用zerorpc，利用的是zeroMQ的messagepack
http://www.zerorpc.io/
http://blog.csdn.net/qq_30242609/article/details/54427676
'''
#这里是server端
import zerorpc
import time

class hellorpc(object):
    def hello(self):
        print(time.localtime())
        return (time.time())

s = zerorpc.Server(hellorpc())
s.bind("tcp://0.0.0.0:4242")
s.run()
