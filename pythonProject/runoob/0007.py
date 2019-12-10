# 字典
dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict2 = {'abc': 456}
dict3 = {'abc': 456, 'def': 789}

print(dict1)
print(dict2)
print(dict3)

print(dict1['Alice'])
print(dict1['Cecil'])

dict1['Cecil'] = 666
print(dict1['Cecil'])

print(str(dict1))

# fromkeys()函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
seq = ('name', 'age', 'sex')

dict1 = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dict1))

dict2 = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dict2))

dict1 = {'Name': 'Runoob', 'Age': 27}

print("Age 值为 : %s" % dict1.get('Age'))
print("Sex 值为 : %s" % dict1.get('Sex', "默认值：24"))
print('Name' in dict1)
print("Item : %s" % dict1.items())
print("Key : %s" % dict1.keys())
print("Value : %s" % dict1.values())
