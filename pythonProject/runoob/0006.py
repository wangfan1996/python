# 元祖

tup1 = ('Google', 'Runoob', 1997, 2000);
tup2 = (1, 2, 3, 4, 5)
#  不需要括号也可以
tup3 = "a", "b", "c", "d"
print(type(tup3))
# 创建空元祖
tup4 = ()
print(tup4)
print(type((10)))
print(type((10, )))
# 元祖值不允许修改
tupTest = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupTest)
print("tupTest[0]: ", tupTest[0])
print("tupTest[1:5]: ", tupTest[1:5])

print(3 in tupTest)

for x in tupTest:
    print(x, end=' ')


