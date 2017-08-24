import socket


HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
addr_self = s.getsockname()#get the client ip(host,port)
addr_to = s.getpeername()#get the server ip

while True:
    user_input = input('msg to send'+str(addr_self)+'to'+str(addr_to)+':').strip()#remove whith space in the str
    s.sendall(user_input.encode())#without encode(), the code would be wrong 
    data = s.recv(1024)
    print('Received',repr(data))
    
s.close()