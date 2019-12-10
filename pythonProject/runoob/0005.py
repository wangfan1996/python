# 列表

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print(list1[0])

print(list1[1:5])

print(list2)
list2[2] = 20
print(list2)
del list2[2]
print(list2)
print(len(list2))

list4 = [['a', 'b', 'c'], [1, 2, 3]]
print(list4)
print(max(list2))
print(min(list2))

listTest = [2, 3, 4]
print(listTest)
listTest.append(5)
print(listTest)
a = listTest.pop()
print(a)

listTest.extend([5, 6, 7, 5])
print(listTest)
print(listTest.count(5))
print(listTest.index(5))
listTest.insert(0, 1)
print(listTest)
listTest.insert(1, 100)
print(listTest)
listTest.reverse()
print(listTest)
