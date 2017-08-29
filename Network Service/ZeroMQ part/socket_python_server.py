#-*- coding:utf-8 -*-

import socket
import json
import os

def socket_bind():
    addr = ('localhost',6379)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(addr)
    #使用listen方法进行监听，5代表最大连接数为5个
    s.listen(5)
    return s

def get_bytes():
    # 在测试过程中遇到一个问题，在cmd和ide中os.getcwd（）得到的路径不同
    # 因为os.getcwd（）在cmd中得到的应该是cmd.exe所在的目录，因为此时的工作目录与ide的工作目录不同
    # 解决方法是用os.path.dirname(__file__)
    #base_path = os.getcwd()
    #print(os.path.dirname(__file__))
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path,"configuration.xml")  
    print(file_path)
    # 此处有必要加上encoding='utf-8'否则容易报错
    file_object = open(file_path,'r',encoding='utf-8')
    xml_str = file_object.read()
    
    xml_bytes = xml_str.encode(encoding='utf-8')
    
    return xml_bytes


if __name__ == '__main__':
    s = socket_bind()
    xml_bytes = get_bytes()
    # 传输的数据的基本信息用bytes_info来记录
    # 消息类型用四位二进制来表示，可以表示16种不同的数据类型
    # 用8位十进制来表示数据长度
    # 发送数据前先发送bytes_info
    # bytes不支持索引，可以用bytearray或者str，这里选择str
    str_info = '0000'+str(xml_bytes.__len__()).zfill(8)
    bytes_info = str_info.encode('utf-8')

    #print(xml_bytes.decode())
    while True:
        connection,address = s.accept()
        print("Client ip is",address)
        try:
            connection.settimeout(5)
            #此处必须为connection.send,而不是s.send，之前用s.send报错
            #还是搞不清楚send和sendall的区别，我发送一个1260198bytes的数据也是能够以此发送过去
            connection.sendall(bytes_info)
            print('send byte_info')
            connection.sendall(xml_bytes)
            #print("$$$",isinstance(xml_bytes,unicode))
            print('send xml_byte')
        except socket.timeout:
            print('time out')
    
    