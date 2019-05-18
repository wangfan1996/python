import requests, json, pymysql, time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjEsImlhdCI6MTU1NzIxOTAyMSwiZXhwIjozMzU3MjE5MDIxfQ.hiyd_2WmhSf9oyf1VAFEur1CgroKg8efMgw6vZ7OKgU'
headers = {'token':token}
typeGet = requests.get("http://192.168.6.107/jwxslist/test",headers=headers)
dictTypeGet = typeGet.json()
data = dictTypeGet['data']
item = []
for x in data:
    item.append(list(x.values()))
db = pymysql.connect("","","" )
cursor = db.cursor()
sql = "INSERT INTO user(name,user,pwd,powerpwd,birth,qq,phone) VALUES (%s,%s,%s,%s,%s,%s,%s)"
try:
   cursor.executemany(sql,item)
   db.commit()
except:
   db.rollback()
db.close()
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
