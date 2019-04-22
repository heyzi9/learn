# 导入csv库
import csv

# 打开文件
# file = open('data.csv', 'r', encoding='utf-8', errors='ignore')
# csv_file = csv.reader(file)

# 通过对元素遍历来逐行输出
# for i in csv_file:
#     print(i)

#要写入的文件
header = ["name","gender","score"]
file_1 = ["zhang_san","male"]
file_2 = ["Li_si","male","80"]

# 创建，不加newline也行，但是会多出一行空行
csvFile = open("writer.csv","w",newline="")
writer = csv.writer(csvFile)

#写入内容
writer.writerow(header)
writer.writerow(file_1)
writer.writerow(file_2)

#关闭
csvFile.close()