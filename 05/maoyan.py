# 导入库
from selenium import webdriver
import time
import csv

# 序号列表
numbers_list = [0,10,20,30,40,50,60,70,80,90]

# 写入url字典
url_list = []
for i in numbers_list:
    url = "https://maoyan.com/board/4?offset=%d"%i
    url_list.append(url)
    print("获取地址:%s"%url)

# 打开浏览器
dr = webdriver.Chrome()

# 打开csv文件
csv_file = open("writer.csv","w+",newline='',encoding='utf-8-sig')
writer = csv.writer(csv_file)

# 访问一级页面
for i in url_list:
    dr.get(i)
    time.sleep(1)
    print("正在链接为%s的页面"%i)

    #循环嵌套，对每个页面中的链接再次进行获取操作
    for j in range(1,10):
        #从一级页面获取信息
        #获取演员
        xpath2 = '//*[@id="app"]/div/div/div[1]/dl/dd[%d]/div/div/div[1]/p[2]'%j
        actor = dr.find_element_by_xpath(xpath2).text

        #获取分数
        xpath3 = '//*[@id="app"]/div/div/div[1]/dl/dd[%d]/div/div/div[2]/p'%j
        score = dr.find_element_by_xpath(xpath3).text

        #获取标题
        xpath1 = '//*[@id="app"]/div/div/div/dl/dd[%d]/div/div/div[1]/p[1]/a'%j
        title = dr.find_element_by_xpath(xpath1).text

        # 访问二级页面
        # 获取电影介绍
        dr.find_element_by_xpath(xpath1).click()
        xpath4 = '//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/span'
        introduce = dr.find_element_by_xpath(xpath4).text

        # print('电影标题:%s'%title)
        # print('演员:%s'%actor)
        # print('分数:%s'%score)
        # print('简介:%s'%introduce)

        # 拼接
        text = []
        text.append(title)
        text.append(actor)
        text.append(score)
        text.append(introduce)

        # 写入csv
        writer.writerow(text)
        print("----正在获取第%s条"%j)
        #返回初始页面
        dr.get(i)

# 关闭浏览器
print("all_done")
dr.close()