import pymongo
# https://www.jianshu.com/p/71f915b01bdf
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# 数据库列表
dblist = myclient.list_database_names()
print(dblist)

school = myclient["School"]
# 集合列表
collist = school.list_collection_names()
print(collist)

# 创建集合
student = school["student"]
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
# 插入集合
x = student.insert_one(mydict) 
print(x.inserted_id)

teacher = school["teacher"]
# 查询一条数据
x = teacher.find_one()
print(x)

xall = teacher.find()
for x in xall:
    print(x)
