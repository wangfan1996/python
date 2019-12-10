import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb = myClient['school']
myCol = myDb['sites']

# 查询集合中的一条数据
x = myCol.find_one()
print(x)
print('*' * 100)
# 查询所有数据find
for x in myCol.find():
    print(x)
print('*'*100)
# 查询指定字段的数据
for x in myCol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    print(x)
print('*'*100)
for x in myCol.find({}, {"url": 1}):
    print(x)
print('*' * 100)
# 指定条件查询
myQuery = {"name": "RUNOOB"}
myDoc = myCol.find(myQuery)
for x in myDoc:
    print(x)
print('*' * 100)
# 高级查询 name第一个字母大于H
myQuery = {"name": {"$gt": "H"}}
myDoc = myCol.find(myQuery)
for x in myDoc:
    print(x)
print('*' * 100)
# 返回指定条数记录
myResult = myCol.find().limit(3)
for x in myResult:
    print(x)
print('*' * 100)
