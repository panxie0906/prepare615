# Just for test
# Put the code of Server and Client in on .py
# Communication between threads

import zmq
import time
import threading

def req_function():
    socket = context.socket(zmq.REQ)
    socket.connect(addr)
    
    print("Sending request",request," to server...")
    socket.send("Hello".encode('utf-8'))
    message = socket.recv()
    print(message)
        
def rep_function():
    socket = context.socket(zmq.REP)
    socket.bind(addr)
    
    message = socket.recv()
    while message:
        print(message)
        socket.send("World".encode('utf-8'))
        message = socket.recv()


if __name__ == "__main__":
    addr = "tcp://127.0.0.1:5555"
    context = zmq.Context();    
    
    try:
        start_time = time.time();
        
        thread_rep = threading.Thread(target=rep_function)
        thread_rep.start()
        
        for request in range(1,3):
            thread_req = threading.Thread(target=req_function)
            thread_req.start()
            thread_req.join() 
        
    except(KeyboardInterrupt,SystemError):
        print("Receive ERROR or KeyboardInterrupt")
    finally:
        context.term()
        
        
    