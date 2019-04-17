# 导入库
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import phantomjs

# 数据写入CSV函数
def write(item):
    with open(r"F:\git\python\learn\jr2.csv","a")as f:
        writer = csv.writer(f)
        try:
            writer.writerow(item)
        except:
            print("error")

# 获取信息函数
def getinfo():
    id_ = dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[1]')
    time_ = dr.find_element_by_xpath('//*/div[@class="article-sub"]/span[2]')
    title_ = dr.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/h1')
    text_ = dr.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div[2]')
    item = [id_.text,time_.text,title_.text,text_.text]
    return item

#打开浏览器，设置隐式等待，打开页面
url = "https://www.toutiao.com/search/?keyword=selenium"
dr = webdriver.Chrome()
# dr = webdriver.PhantomJS()
dr.implicitly_wait(2)
dr.get(url)

# 给页面留下足够的时间加载
time.sleep(1)

# 刷新出足够的条数，保证加载到底
for i in range(2000):
    #相当于一直按着down键，下拉页面
    ActionChains(dr).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
    print(f'下拉已完成{i}次')

# 再次留下时间加载，因不确定最后刷新到哪，因此不用显示等待
time.sleep(1)
url_ = dr.find_elements_by_css_selector('.title')
print(url_)

#链接列表
url_list = []
for i in url_:
    url_list.append(i.get_attribute('href'))
print(url_list)

#使用try，except接收报错
for i in url_list:
    try:
        dr.get(i)
        time.sleep(0.5)
        write(getinfo())
        dr.get(url)
        print('已完成写入')
    except:
        print("error")
print("all_done")
