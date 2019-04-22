from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import Element

dict = {"name":"zhang_san","gender":"female","phone_number":"01234567890","note":"none"}

# 转换函数
def convert(tag_name,dict):
    # 建立一个XML
    elem = Element(tag_name)
    #双值循环取出字典中的key和value
    for key,value in dict.items():
        print(key,":",value)
        #为key建标签
        xml_elem = Element(key)
        # 将key的值赋给这个标签
        xml_elem.text = str(value)
        # 添加进xml文件
        elem.append(xml_elem)
    return elem

# 字典转换
dict_convert = convert("test",dict)
print("------------------------------------")
print(dict_convert)

#转换为标准可读的xml
print(tostring(dict_convert))
#设置最外层标签的属性
dict_convert.set('id_number','01234567890')
#再次输出
print(tostring(dict_convert))