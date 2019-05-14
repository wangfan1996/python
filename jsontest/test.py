import json

data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
print(data)

json_str = json.dumps(data)
print(json_str)

json_obj = json.loads(json_str)
print(json_obj)

