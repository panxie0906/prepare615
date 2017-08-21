# Reference:http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html

import zmq
import sys
import time
import random

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
    print("the topic is %d, and the messageData is %d"%(topic,messageData))
    socket.send_string("%d %d"%(topic,messageData))
    time.sleep(1)
