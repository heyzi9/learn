#导入库
import pymysql

# 创建数据库
conn = pymysql.connect(host='localhost',port=3306,db='test',
                       user='root',password='5570852mu',charset='utf-8')
cur = conn.cursor()

#查询原数据
select="SELECT * FROM user_info"
cur.execute(select)
