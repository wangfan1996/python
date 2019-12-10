import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
dbList = myClient.list_database_names()
print(dbList)
if 'school' in dbList:
    print('数据库已存在')

# 创建一个数据库
myDb = myClient['school']
# 创建一个集合
myCol = myDb['sites']

colList = myDb.list_collection_names()
if 'sites' in colList:
    print('集合已存在')

# 插入集合

myDict = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}
# insert_one() 方法返回 InsertOneResult 对象，该对象包含 inserted_id 属性，它是插入文档的 id 值
# 插入文档时没有指定 _id，MongoDB 会为每个文档添加一个唯一的 id。
x = myCol.insert_one(myDict)
print(x)
print(x.inserted_id)
myList = [
  {"name": "TaoBao", "alexa": "100", "url": "https://www.taobao.com"},
  {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
  {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
  {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
  {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]
# 集合中插入多个文档使用 insert_many() 方法，该方法的第一参数是字典列表。
x = myCol.insert_many(myList)
# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
# 指定id插入
myList = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google 搜索"},
    {"_id": 3, "name": "Facebook", "address": "脸书"},
    {"_id": 4, "name": "Taobao", "address": "淘宝"},
    {"_id": 5, "name": "Zhihu", "address": "知乎"}
]
x = myCol.insert_many(myList)
print(x.inserted_ids)
