import requests, json
# 传递参数
payload = {'user':'admin','pwd':'wangfan'}
# 发送请求
r = requests.post("http://118.89.242.170:8003/login/login",payload)
# 响应状态玛
# print(r.status_code)
# Requests附带一个内置的状态码查询对象
# print(requests.codes.ok)
# 返回头信息(Chrome浏览器->Network->Headers->Response Headers(view parsed))
# print(r.headers)
# 返回变量类型
# print(type(r.headers))
# 计算字典元素个数，键的总数
# print(len(r.headers))
# 编码信息
# print(r.encoding)
# 获取网页内容，返回字符串
# print(r.text)
# 以字节方式显示
# print(r.content)
# Requests 中内置的JSON解码器处理JSON数据
dictRes = r.json()
# Id = dictRes['data']['Id']
# user = dictRes['data']['user']
# pwd = dictRes['data']['pwd']
token = dictRes['data']['token']
# print(token)
headers = {'token':token}
typeGet = requests.get("http://118.89.242.170:8003/type/1",headers=headers)
dictTypeGet = typeGet.json()
data = dictTypeGet['data']
# print(dictTypeGet)
# 字典遍历
for key,values in dictTypeGet.items():
    pass
    #print(key,values)

for x in data:
    for key,values in x.items():
        print(key,"==>",values)



