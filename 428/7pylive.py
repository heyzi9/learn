# 导入库
import os
from pybloom_live import BloomFilter

# 数据库文件
animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
           'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear', 'chicken', 'dolphin', 'donkey', 'crow',
           'crocodile', 'testadd']

# 判断文件是否存在
# 存在时读取，不存在时创建
is_exist = os.path.exists('test.blm')
if is_exist:
    bf = BloomFilter.fromfile(open('test.blm','rb'))
# 若没有该文件则创建bf对象
else:
    bf = BloomFilter(20000,0.001)

# 如果存在则跳过，否则写入
for i in range(10):
    if i in bf:
        print('pass')
        pass
    else:
        print('add %s'%i)
        bf.add(i)
        bf.tofile(open('test.blm','wb'))

#判断是否存在
for i in range(20):
    if i in bf:
        print("written")
    else:
        print("unwritten")