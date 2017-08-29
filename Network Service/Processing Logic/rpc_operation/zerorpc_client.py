#-*- coding:utf-8 -*-

#zerorpc Client

'''
http://rfyiamcool.blog.51cto.com/1030776/1254000/
经过测试
1、c.hello() 返回的值是hello（）实际所在主机函数的return值
2、单线程条件下，1s内能够调用16次，大部分时间应该是消耗在函数本身的耗时那里
   也就是说，不适用于高速的要求，本方案中，对于xml的解析和生成是可以考虑使用这个方法的
'''
import zerorpc
import time

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
start = time.time()
sum = 0
while time.time()<start+1.0:
    sum +=1
    print(sum,"----->",c.hello())