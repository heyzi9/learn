# 导入库
import base64
import nltk

# 定义字符串
string = b'admin'

# encode 表示编码，decode表示解码
encoded = base64.b64encode(string)
decoded = base64.b64decode(encoded)

# 打印
print(encoded)
print(decoded)
nltk.download()