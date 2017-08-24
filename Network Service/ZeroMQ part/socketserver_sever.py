import socketserver

class mysockserver(socketserver.BaseRequestHandler):#must inherit from socketserver.BaseRequestHandler
    
    def handle(self): #must have a method handle
        print("New connection:",self.client_address)
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print('Client Data:',data.decode())
            self.request.send(data.upper())
            
if __name__ == '__main__':
    HOST = '' #means listen to all the ips
    PORT = 50007
    server = socketserver.ThreadingTCPServer((HOST,PORT),mysockserver)
    
    server.serve_forever()
    