# 基础语法

import sys

strHelloPython = "Hello Python"
print(strHelloPython)

if True:
    print('true')
else:
    print('false')

itemOne = 1
itemTwo = 2
itemThree = 3

total = itemOne + \
        itemTwo + \
        itemThree

print(total)

word = '字符串'
sentence = '这是句子。'
paragraph = """这是段落，
可以自由换行"""

print(word)
print(sentence)
print(paragraph)

x = "a"
y = "b"
print(x)
print(y)
print(x, end=' ')
print(y, end=' ')
print()

for i in sys.argv:
    print(i)

print('python路径为', sys.path)

