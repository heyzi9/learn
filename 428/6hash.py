# 导入哈希算法库
import hashlib

# MD5 加密
md5_1 = hashlib.md5()
md5_1.update(b"I'm using md5 in python")#上传需要加载的字符串
print(md5_1.hexdigest())# 计算结果值

# 如果数据量很大，可以分块多次调用update(),结果不变
md5_2 = hashlib.md5()
md5_2.update(b"I'm using md5")
md5_2.update(b" in python")
print(md5_2.hexdigest())

# SHA1 加密
sha1 = hashlib.sha1()
sha1.update(b"I'm using md5 in python")
print(sha1.hexdigest())