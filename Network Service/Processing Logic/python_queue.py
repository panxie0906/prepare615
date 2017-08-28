#-*- coding:utf-8 -*-

import queue

'''
python queue有三种构造函数
class Queue.Queue(maxsize)
class Queue.LifoQueue(maxsize)
class Queue.PriorityQueue(maxsize)
分别对应
FIFO先进先出队列
LIFO先进后出队列
优先级队列，优先级越低越先出来
'''

def queue_op():
    # 如果超出队列长度就会发生很诡异的反应
    # maxsize<1代表无限
    # 想要实现环状的队列可以自己自定义实现
    myqueue = queue.Queue(3)
    myqueue.put(10)
    myqueue.put('hhhhhh')
    myqueue.put(3)
    
    while not myqueue.empty():
        print(myqueue.get())
        
if __name__ == '__main__':
    queue_op()