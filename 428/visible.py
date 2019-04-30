# 确定元素是否可见
# 导入库
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

# 打开网站
dr = webdriver.Chrome()
dr.get("http://172.16.21.137")

# 延时两秒，输入账号密码登录
time.sleep(2)
name = dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/section[1]/input')
pwd = dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/section[2]/input')
name.send_keys('yjm')
pwd.send_keys('12345678')
dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button').click()

# 延时5秒关闭浏览器
time.sleep(5)
print(EC.visibility_of_element_located('1dsfsgsxvd'))
dr.close()