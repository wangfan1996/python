import pymysql

# 打开数据库连接
db = pymysql.connect("ip地址","账号","密码","数据库" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

# SQL 查询语句
sql = "SELECT * FROM ch_token"
cursor.execute(sql)
token = cursor.fetchall()


print ("Database version : %s " % data)

for item in token:
    Id = item[0]
    userId = item[1]
    token = item[2]
    insertTime = item[3]
    print("Id=%d,userId=%d,token=%s,insertTime=%s"%(Id,userId,token,insertTime))

# 关闭数据库连接
db.close()
