# 导入库
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

# 打开页面
dr = webdriver.Chrome()
dr.get("http://172.16.21.137")
# time.sleep(1)
# title = EC.title_contains("爱家")
# print(title(dr))

# 输入账号和密码,点击登录
def login(name,psd):
    username = dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/section[1]/input')
    password = dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/section[2]/input')
    username.send_keys(name)
    password.send_keys(psd)
    dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button').click()

login('yjm','12345678')
# 等待2s
time.sleep(2)
key1 = dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/strong').text
print(key1)
dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[3]/div/i').click()
dr.find_element_by_xpath('//*[@id="dropdown-menu-8153"]/li[3]').click()
# dr.close()

#等待3秒
time.sleep(3)
login('mumu','12345678')
time.sleep(2)
key2 = dr.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/strong').text
print(key2)
print( key1 == key2)
dr.close
