#-*- coding:utf-8 -*-

import redis

'''
搞清楚要存储在数据库中数据的种类和结构
一个message用Hash表示比较好
Hash可以有3种的结构化表示方法
1-----> key（eg：ID）:序列化的value对象（使用key获取对象，必须使用反序列化）
2-----> key（eg：ID+标签属性等关键词）：value
3-----> key：另一个Hash（field：value）
List
相当于一个key一个list作为其value
set和zset类似于list
'''

'''
至于持久化等一些策略在conf中进行设置，不使用具体的command
'''

'''
redis服务器的windows版本可以在微软的github下载，不提供32位版本需要下载源码再编译成32位版本
redis-py是redis的python客户端，也就是说，本文件代码实际上就是一个客户端
redis-py 有两个类Redis和StrictRedis两个类，其中Redis类是StrictRedis的子类
Redis连接方式有两种，一种是单个的一种是线程池的

之前把这个文件命名为redis.py最后导致module is not callable，改个名就行

线程池有利于连接的复用，可以实现多个实例共用一个连接
'''

# 项目中对redis的操作必须具体结合xml和message的解析
# 单个的光说操作没什么意义，因为其操作其实就是那么些动作，顶多加上事务或者是流水线

def get_connect():
    # R = redis.Redis(host='127.0.0.1',port=6379)
    pool = redis.ConnectionPool(host='localhost',port=6379,db=0,password=None)
    R = redis.StrictRedis(connection_pool=pool)
    
    return r


# 发现这里有个问题，无论是subscribe还是publish都会有个延时，如果在语句下立即接一个get_message往往会
# 得到一个none，但是如果放的太后也会错过message而得到none
# 这让我觉得redis中使用订阅发布模式或许不是一个很好的选择
def pub_sub(R):
    # 订阅发布模式
    p = R.pubsub()
    #p.subscribe('channel 1','channel 2')
    p.psubscribe('channel*')
    R.publish('channel 1','channel 1 data')
    R.publish('channel 2','channel 2 data')
    print(p.get_message())
    print(p.get_message())    
    print(p.get_message())
    print(p.get_message())
    while p.get_message()!=None:
        print(p.get_message())
    p.subscribe(**{'my-channel':my_handler})
    R.publish('my-channel','my-channel data')
    p.get_message()
    p.get_message()
# 使用回调函数的订阅发布
def my_handler(message):
    print('MY HANDLER:  ', message['data'])

if __name__ == '__main__':
    R = get_connect()
    pub_sub(R)
