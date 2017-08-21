# Reference:http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html

import zmq
import sys

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
    print("the topic is %s, the messageData is %s"%(topic,messageData))