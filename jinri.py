# 导入库 2-4是显示等待用到的库
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 整理为函数
def getinfo():
    id_ = dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[1]')
    time_ = dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[2]')
    title_ = dr.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/h1')
    text_ = dr.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div[2]')
    item = [id_.text,time_.text,title_.text,text_.text]
    return item

# 打开浏览器和百度风云榜
dr = webdriver.Chrome()
dr.get("http://top.baidu.com")

# 延时1s，根据xpath获取标题并传到字典hw_dirt里
# time.sleep(1)
hw_dirt = []
for i in range(10):
    x = '//*[@id="hot-list"]/li['+str(i+1)+']/a[1]'
    # print(x)
    value = dr.find_element_by_xpath(x).get_attribute('title')
    hw_dirt.append(value)
    # print(dr.find_element_by_xpath(xpath).get_attribute("title"))

# print(hw_dirt)
# 获取字典的第一个元素
keyword = hw_dirt[0]

# 搜索第一个关键词的新闻
URL = 'https://www.toutiao.com/search/?keyword=%s'%keyword
dr.get(URL)


# Xpath拼接
XPath = '//*[@id="J_section_0"]/div/div/div[1]/div/div[1]/a/span'

# 显示等待调用
try:
    WebDriverWait(dr,20,0.5).until(EC.presence_of_element_located((By.XPATH,XPath)))
finally:
    dr.find_element_by_xpath(XPath).click()

# 给页面留足时间加载，防止被禁ip
time.sleep(1)

# 获取所有的句柄
all_handles = dr.window_handles

# 跳转到最后一个句柄-刚刚打开的页面
dr.switch_to.window(all_handles[-1])

# 获取信息
info = getinfo()
print(info)