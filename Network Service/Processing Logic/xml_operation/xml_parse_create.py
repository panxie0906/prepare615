#-*- coding:utf-8 -*-

# message的格式是由ICD.xml定义的
# 中间件部分需要处理的xml文件具体分析可以如下
# ICD.xml从上位机socket部分接收过来，用来查询message数据格式
# Device.xml不做处理直接传输到上位机部分即可
# configuration.xml用来查询消息的通道绑定，建议可以将具体某个服务节点的所有绑定的message都存入一个列表中
# 利用好xpath
# 至于xml文件的生成，暂时大略了解即可，因为还不知道如何扫描硬件

import xml.etree.ElementTree as ET


def read_xml(xml_path):
    '''
        root is an Element
        Element is a python class, class xml.etree.ElementTree.Element(tag,attrib={},**extra)
        Reference:https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element
        As an Element, root has tag,and attributes
        tag is a string, represents the element name
        attrib is an optional dictionary, containing element attributes
    '''
    # root = ET.fromstring(xml_path) equals to the following two lines of code
    tree = ET.parse(xml_path)
    root = tree.getroot()
    print(root.tag,"  ",root.attrib)
    return root
                             
    
if __name__ == '__main__':
    in_xml_path = r"baspools.xml"
    xml_to_dic(read_xml(in_xml_path))