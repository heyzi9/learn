# 导入库
from xml.etree import ElementTree as et

# root = et.parse(r'D:/test.xml')
#定义字符串
xml_string = b'<test><name>zhang_san</name><gender>female</gender><phone_number>0123' \
             b'4567890</phone_number><note>none</note></test>'
#从文本中获取XML
root = et.fromstring(xml_string)

#instance 1
print('*****================================*****')
#列表形式输出的内存地址
for i in list(root):
    print(i.tag,i.text)

# instance 2
print('*****================================*****')
test_person = root.getiterator('test')
# 用来输出内容
for i in test_person:
    for j in i:
        print(j.tag,j.text)

# instance 3
print('*****================================*****')
#返回的是一个列表
find_node2 = root.findall('name')
print(find_node2[0],find_node2[0].tag,find_node2[0].text)

# instance 4
print('*****================================*****')
# 查找获得的第一个
find_node = root.find('name')
print(find_node,find_node.tag,find_node.text)


