import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb = myClient['school']
myCol = myDb['sites']

myQuery = {"name": "TaoBao"}
# 删除一个文档
myCol.delete_one(myQuery)
# 删除后输出
for x in myCol.find():
    print(x)

# 删除多个文档
myQuery = {"name": {"$regex": "F"}}
x = myCol.delete_many(myQuery)
print(x.deleted_count)

# 删除所有文档
x = myCol.delete_many({})
print(x.deleted_count, "个文档已删除")
# 删除集合
myCol.drop()
