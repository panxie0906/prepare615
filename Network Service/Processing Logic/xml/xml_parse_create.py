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
    #root = ET.fromstring(xml_path) equals to the following two lines of code
    tree = ET.parse(xml_path)
    root = tree.getroot()
    print(root.tag,"  ",root.attrib)
    return root

def recursion_dict_xml(value):
    if value.find(".//")==None:
        dict_init = {}
        print(value.tag)
        value_parent = value.find("..")
        for key,key_value in value_parent.findall():
            dict_init
    
        
    return 1

def xml_to_dic(root):
    dict_result = {}
    
    '''
    itera = root.iter()
    for i in itera:
        print(i.tag)
    # ergodic
    '''
    '''while True:
        try:
            i = itera.next()
            print(i)
        except StopIteration,e
        break   
        
    '''

    for key,value in enumerate(root):
        print(value.tag)
        #recursion_dict_xml(value)
        key = str(key)        
        #for item in value:
         #   print(item.tag,"   ",item.text)
        value_tmp = value
        while value_tmp.find(".//")!=None:
            value_tmp = value.find(".//")
        while value_tmp.find("..")!=None:
            value_tmp = value_tmp.find("..")
            dict_init = {}
            for i in value_tmp.findall():
                dict_init[i.tag] = i.text
                
                
    
if __name__ == '__main__':
    in_xml_path = r"baspools.xml"
    xml_to_dic(read_xml(in_xml_path))