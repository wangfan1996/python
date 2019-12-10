import requests

data = {'name':'tom','age':'22'}
response = requests.post('http://httpbin.org/post', data=data)
# print(response.text)

# 获取cookie
responseCookie = requests.get('http://www.baidu.com')
print(responseCookie.cookies)
print(type(responseCookie.cookies))
for k, v in responseCookie.cookies.items():
    print(k + ':' + v)
