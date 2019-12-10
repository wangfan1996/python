import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb = myClient['school']
myCol = myDb['sites']

# 升序排序
myDoc = myCol.find().sort("alexa")

for x in myDoc:
    print(x)

print('*'*100)
myDoc = myCol.find().sort("alexa", -1)
for x in myDoc:
    print(x)
print('*'*100)

