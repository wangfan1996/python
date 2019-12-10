import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb = myClient['school']
myCol = myDb['sites']

myQuery = {"alexa": "100"}
newValues = {"$set": {"alexa": "12345"}}
# update_one() 方法只能修匹配到的第一条记录，如果要修改所有匹配到的记录，可以使用 update_many()
myCol.update_one(myQuery, newValues)

for x in myCol.find():
    print(x)
print('*'*100)

# 查找F开头的name将alexa改为6666
myQuery = {"name": {"$regex": "F"}}
newValues = {"$set": {"alexa": "6666"}}
myCol.update_many(myQuery, newValues)

for x in myCol.find():
    print(x)
print('*'*100)

