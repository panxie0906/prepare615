# coding=utf-8
# Reference:http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html

import zmq
import sys
import time
import random
import threading


def Publisher(func):    
    port = "5556"
    
    # if possible, read the parameter from command line
    if len(sys.argv)>1 :
        port = sys.argv[1]
        int(port)
    
    # create publisher with socket type zmq.PUB
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:%s"%port)
    
    # the publisher sends the message 
    while True:
        # the topic can be parsed from message receive via http
        topic = random.randrange(9999,10005)
        messageData = random.randrange(1,125)-80
        print("%s: the topic is %d, and the messageData is %d"%(func,topic,messageData))
        socket.send_string("%d %d"%(topic,messageData))
        time.sleep(1)

def Subscriber(func):  
    port = "5556"
    
    # if possible, read the parameter from command line
    # the subcriber can subcribe more than one publisher
    if len(sys.argv)>1:
        port = sys.argv[1]
        int(port)
    # we suppose that a second publisher is possible    
    if len(sys.argv)>2:
        port1 = sys.argv[2]
        int(port1)
        
    # create publisher with socket type zmq.SUB
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    
    # connect to server
    socket.connect("tcp://localhost:%s"%port)
    
    if len(sys.argv)>2:
        socket.connect("tcp://localhost:%s"%port1)
        
    '''
    In our example, the subcirber subcribes specific zip codes 
    The current version of zmq supports filtering of messages based on topics at subscriber side
    This is usually set via socketoption
    '''
    topics = ["10001","10002"]
    for topic in topics:
        socket.setsockopt_string(zmq.SUBSCRIBE,topic)
    
    # try five times to verify the code   
    for updates in range(5):
        message = socket.recv()
        topic,messageData = message.split()
        print("%s: the topic is %s, the messageData is %s"%(func,topic,messageData))
        
# creat threading
threads = []
tpub = threading.Thread(target=Publisher,args=(u'Publisher',))
threads.append(tpub)
tsub1 = threading.Thread(target=Subscriber,args=(u'Sub1',))
threads.append(tsub1)
tsub2 = threading.Thread(target=Subscriber,args=(u'Sub2',))
threads.append(tsub2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    
    t.join()