#the server part of request-reply

import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print ("receive message is ",message)
    
    time.sleep(1)
    
    socket.send("world".encode('utf-8'))