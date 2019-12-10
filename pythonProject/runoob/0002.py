# 基本数据类型

counter = 100
miles = 1000.00
name = 'WangFan'

print(counter, miles, name)

a = b = c = 1

print(a, b, c)

a, b, c = 1, 2, 'WangFan'

print(a, b, c)

"""
不可变数据
    Number 数字
    String 字符串
    Tuple 元祖
可变数据
    List 列表
    Set 集合
    Dictionary 字典
"""

# Number
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))

# isinstance 和 type
# type不会认为子类是一种父类类型
# issubclass会认为子类是一种父类型


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))

print(isinstance(B(), A))

print(type(A()) == A)
print(type(B()) == A)

# String
"""
从后面索引： -6 -5 -4 -3 -2 -1
从前面索引：  0  1  2  3  4  5
            a  b  c  d  e  f   
从前面截取： :  1  2  3  4  5  :
从后面截取： : -5 -4 -3 -2 -1  :
"""

strStr = 'abcdef'
print(strStr[0:-4])    #ab
print(strStr[3:-1])    #de
print(strStr[2:])      #cdef

# 不让反斜杠发送转义
print('wa\ngfan')
print(r'wa\ngfan')

# List
# 索引值以0为开始值，-1位从末尾的开始位置
listList = ['abcd', 786, 2.23, 'runoob', 70.2]
tinyList = [123, 'runoob']

print(listList)  # 输出完整列表
print(listList[0])  # 输出列表第一个元素
print(listList[1:3])  # 从第二个开始输出到第三个元素
print(listList[2:])  # 输出从第三个元素开始的所有元素
print(tinyList * 2)  # 输出两次列表
print(listList + tinyList)  # 连接列表

# 和字符串不一样，列表元素是可以改变的
a = [1, 2, 3, 4, 5, 6]
print(a)
a[0] = 9
print(a)
a[2:5] = [13, 14, 15]
print(a)
a[2:] = []
print(a)
"""
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。
"""

strLang = 'my name is wang fan'
listName = strLang.split(' ')
print(listName)
listNameReversal = listName[-1::-1]
print(listNameReversal)
strJoin = "-".join(listNameReversal)
print(strJoin)

# 元祖Tuple
# 修改元组元素的操作是非法的

testTuple = ('wang', 786, 2.23, 'fan', 70.2, True, False)
tinyTuple = (123, 'abc')

print(testTuple)
print(type(testTuple))
print(testTuple[0])
print(testTuple[1:3])
print(testTuple[2:])
print(testTuple[-1::-1])
print(testTuple[::-1])
print(testTuple * 2)
print(testTuple + tinyTuple)

# 空元祖
tup1 = ()
# 一个元素,需要在元素后面添加逗号
tup2 = (20, )
print(tup1)
print(tup2)
"""
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
"""

# Set集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

if 'Rose' in student:
    print('Rose在集合中')
else:
    print('Rose不在集合中')

# set可以进行集合操作
a = set('abracadabra')
b = set('alacazam')
print(a)
# a 和 b 差集
print(a - b)
# a 和 b 并集
print(a | b)
# a 和 b 交集
print(a & b)
# a 和 b 中不同时存在的元素
print(a ^ b)

# 字典
testDict = {}
testDict['name'] = '张三'
testDict[2] = 2
print(testDict)
print(testDict.keys())
print(testDict.values())

# 常用函数
print(ord('A'))
print(chr(ord('A')))



























