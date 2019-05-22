# 导入库
from selenium import webdriver
import time
import csv

# 序号列表，用来翻页
number_list = [0,25,50,75,100,125,150,175,200,225,250]
# number_list = [0,25,50]

url_list=[]
# 拼接网址并写入url_list
for i in number_list:
    url = 'https://movie.douban.com/top250?start=%d&filter='%i
    url_list.append(url)
    print("获取地址：%s"%url)

# 打开浏览器
dr = webdriver.Chrome()

# 打开csv文件
csv_file = open("douban.csv",'w+',newline='',encoding='utf-8-sig')
writer2 = csv.writer(csv_file)
writer2.writerow(['电影','演员','评分','介绍'])

#访问一级页面
for i in url_list:
    dr.get(i)
    time.sleep(2)
    print("正在链接为%s的页面"%i)

    #循环嵌套，获取数据
    for j in range(1,26):

        #获取电影名称
        xpath1 = '//*[@id="content"]/div/div[1]/ol/li[%d]/div/div[2]/div[1]/a'%j
        title = dr.find_element_by_xpath(xpath1).text

        #获取评分
        xpath2 = '//*[@id="content"]/div/div[1]/ol/li[%d]/div/div[2]/div[2]/div/span[2]'%j
        score = dr.find_element_by_xpath(xpath2).text

        #访问二级页面
        #获取演员
        dr.find_element_by_xpath(xpath1).click()
        xpath3 = '//*[@id="info"]/span[3]/span[2]'
        actor = dr.find_element_by_xpath(xpath3).text

        #获取简介
        xpath4 = '//*[@id="link-report"]/span[1]'
        introduce = dr.find_element_by_xpath(xpath4).text

        #打印相关信息
        # print("电影：%s"%title)
        # print("演员：%s"%actor)
        # print("评分：%s"%score)
        # print("简介：%s"%introduce)

        #拼接
        text = []
        text.append(title)
        text.append(actor)
        text.append(score)
        text.append(introduce)

        #写入csv
        writer2.writerow(text)
        print("正在获取第%s条"%j)

        #回到一级页面
        time.sleep(1)
        dr.get(i)

#关闭浏览器
print("all_done")
dr.close()