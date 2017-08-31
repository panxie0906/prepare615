#-*- coding:utf-8 -*-

import xmltodict
import collections

'''
class file(object):
http://blog.csdn.net/zhanh1218/article/details/27112467
'''
def read_file_to_str():
    f_path = open("baspools.xml")
    xml_str = f_path.read()
    return xml_str

#xml_dict 是有序字典，根据元素放入的先后顺序决定其在dict中的先后
'''
建立一个ordereddic的方法如下：

d = collections.OrderedDict() #OrderedDict是一个类，d则是其一个实例
d['1'] = 'a'
d['2'] = 'b'
d['3'] = 'c'
print(d)

d1 = {}
d1['1'] = 'a'
d1['2'] = 'b'
d1['3'] = 'c'
print(d1)
看如下输出的特点：
OrderedDict([('1', 'a'), ('2', 'b'), ('3', 'c')])
{'3': 'c', '2': 'b', '1': 'a'}
在python中
花括号对应字典
方括号对应List
括号对应元组
'''
def parse_xml_to_ordereddict(xml_str):
    xml_dic = xmltodict.parse(xml_str)
    print(xml_dic)
    #while xml_dic.__len__()>0:
    #    print(xml_dic.popitem)
    return xml_dic

def list_all_dict(dict_to_list):
    if isinstance(dict_to_list,dict):
        print('True')
        for x in range(len(dict_to_list)):
            list_key = list(dict_to_list.keys())
            print("list_key",list_key)
            temp_key = list_key[x]
            temp_value = dict_to_list[temp_key]
            print("%s:  %s"%(temp_key,temp_value))
            list_all_dict(temp_value)
            

            
def dict_index():
    d = {}
    d['1'] = 'a'
    d['2'] = 'b'
    d['3'] = 'c'
    
    print(d.keys()[1])#dict_keys不能索引

if __name__ == '__main__':
    xml_str = read_file_to_str()
    xml_dic = parse_xml_to_ordereddict(xml_str)
    print(xml_dic.items())
    #list_all_dict(xml_dic)
    #dict_index()
    print(type(xml_dic))
    list_dict(xml_dic)