# 迭代器与生成器
# iter() 和 next()

listTest = [1, 2, 3]
listTest = iter(listTest)
print(next(listTest))
print(next(listTest))
print(next(listTest))

listTest = [1, 2, 3]
listTest = iter(listTest)
for x in listTest:
    print(x, end=" ")

