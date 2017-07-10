#client part of zeroMQ of reply-request 

import zmq
import time

context = zmq.Context()

print("connecting to hello world server ...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(1,10):
    print ("sending request",request,"...")
    #string.encode('utf-8') to solve unicode cannot encode problem
    socket.send("Hello".encode('utf-8'))
    message = socket.recv();
    print ("receive reply",request,"[",message,"]")