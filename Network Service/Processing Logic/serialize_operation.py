#-*- coding:utf-8 -*-

'''
python序列化提供了两个模块pickle和json
其中pickle是python独有的，不能与其他语言交互
因为pickle将数据对象转化为bytes
'''
import pickle
import json
import sys

'''
pickle提供四个函数来序列化和反序列化
dumps&loads，dump&load
前者将内容从磁盘读入到内存再读到一个bytes中
后者接受两个参数，第一个参数为所需序列化的值，后者为文件对象，直接写入到文件中
'''
def pickle_op():
    d = [1,2,3,4]
    d_pickle = pickle.dumps(d)
    for i in d_pickle:
        sys.stdout.write(str(i)+"   ")
    print()    
    
    print(str(pickle.loads(d_pickle)))

'''
json和pickle差不多的使用方式，不过json转化为str
'''
def json_op():
    d = [1,2,3,4]
    d_json = json.dumps(d)
    print(d_json)
    for i in json.loads(d_json):
        sys.stdout.write(str(i)+"   ")
    print()

class student(object):
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
        
def st_to_dict(a):
    return {'name':a.name,'age':a.age,'course':a.course}

#def stlist_to_dic(alist):
#    dict_list = {}
    

def json_classinstance():
    a1 = student('zhangsan','24','math')  
    a2 = student('lisi','23','Chinese')
    
    print(json.dumps(a1,default=st_to_dict))
  #  list_a = [a1,a2]
    
 #   print(json.dumps(list_a,default=stlist_to_dict))

if __name__ == '__main__':
    pickle_op()
    json_op()
    json_classinstance()