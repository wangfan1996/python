import requests

response = requests.get('http://www.baidu.com')
# 打印状态码
print(response.status_code)
# 打印请求url
print(response.url)
# 打印头信息
print(response.headers)
# 打印cookie信息
print(response.cookies)
# 以文本形式打印网页源码
print(response.text)
# 以字节流形式打印
print(response.content)

# 各种请求方式
responseGet = requests.get('http://httpbin.org/get')
responsePost = requests.post('http://httpbin.org/post')
responsePut = requests.put('http://httpbin.org/put')
responseDel = requests.delete('http://httpbin.org/delete')
responseHead = requests.head('http://httpbin.org/get')
responseOpt = requests.options('http://httpbin.org/get')



