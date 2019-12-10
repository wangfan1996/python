import requests

# 基本的get请求
responseGet = requests.get('http://httpbin.org/get')
# print(responseGet.text)
# 带参数的get请求
responseGetParams = requests.get('http://httpbin.org/get?name=wangfan&age=23')
# print(responseGetParams.text)
# 先将参数填写在dict中
data = {
    'name': 'wangfan',
    'age': 20
}
responseGetParams1 = requests.get(url='http://httpbin.org/get', params=data)
# print(responseGetParams1.text)
print(responseGetParams1.json())  # response.json()方法同json.loads(response.text)
print(type(responseGetParams1.json()))

# response = requests.get('http://img.ivsky.com/img/tupian/pre/201708/30/kekeersitao-002.jpg')
# b = response.content
# with open('2.jpg', 'wb') as f:
#     f.write(b)
opItem = [x for x in range(1, 9)]
for x in opItem:
    url = 'http://img.ivsky.com/img/tupian/pre/201708/30/kekeersitao-00' + str(x) + '.jpg'
    response = requests.get(url)
    b = response.content
    with open('img/' + str(x) + '.jpg', 'wb') as f:
        f.write(b)
