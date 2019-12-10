import pymysql

# 安装pip install PyMySQL
# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "python_test")
# 使用cursor()方法创建一游标对象cursor
cursor = db.cursor()
# 使用execute()方法执行SQL查询
cursor.execute('SELECT VERSION()')
# 使用fetchone方法获取单挑数据
data = cursor.fetchone()
print("Database version : %s " % data)
# 关闭数据库连接
db.close()

db = pymysql.connect("localhost", "root", "root", "python_test")
cursor = db.cursor()
sql = """
    CREATE TABLE employ(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT
    )
"""
sql = """
    INSERT INTO employ(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('王', '帆', 23, 'M', 2000)
"""
sql = "INSERT INTO employ(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)" \
      "VALUES('%s', '%s', '%s', '%s', '%s')"\
      % ('张', '三', 23, 'M', 2000)

# 更新
sql = "UPDATE employ SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M',)
cursor.execute(sql)
# 查询
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
sql = """
    SELECT * FROM employ WHERE INCOME > 1000
"""
cursor.execute(sql)
# 获取所有结果
results = cursor.fetchall()
for row in results:
    print("firstName=%s,lastName=%s,age=%s,sex=%s,inCome=%s" % (row[0], row[1], row[2], row[3], row[4]))

# 删除
sql = "DELETE FROM employ WHERE AGE > %s" % (20,)
cursor.execute(sql)
db.close()



