# 导入库
# import random
from selenium import webdriver
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


# 通过random.sample可以以素材随机形成指定数目的list
# 通过''.join可以将list里的元素添加到空串里
# for i in range(30):
#     user_name = ''.join(random.sample("1234567890abcdefg",8)) + "@163.com"
#     print(user_name)

# 使用谷歌浏览器打开网站，停留5s
driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)

# 保存屏幕截图，根据元素坐标在已保存的截图里取出验证码对应区域的图片
driver.save_screenshot("E:/learn.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("E:/learn.png")
img = im.crop((left,top,right,height))
img.save("E:/learn1.png")