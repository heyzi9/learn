# 导入模块
import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password='5570852mu',
                       database='test',port=3306,charset='utf8')
cur = conn.cursor()

print("*****========================================*****")

#使用execute()方法执行SQL查询
#使用fetchone()方法获取单条数据
version = "SELECT VERSION()"
cur.execute(version)
data = cur.fetchone()
print("Database version:%s"%data)

print("*****========================================*****")

select = "SELECT * FROM user_info"
exe_select = cur.execute(select)
# 现在获取所有数据
all_data = cur.fetchall()
print(all_data)

# 向下移动一行，绝对值从数据输出的上一行开始
# mode默认值为相对
cur.scroll(1,mode='absolute')
data1 = cur.fetchone()
print(data1)

# 向上移动两行
# 因为游标现在相当于在输出所有数据的下一行
cur.scroll(-2,mode='relative')
data2 = cur.fetchone()
print(data2)

# 关闭
cur.close()
# 关闭数据库连接
conn.close()

