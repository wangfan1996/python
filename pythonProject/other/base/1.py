from random import randint

# 列表生成式
data = [randint(-10, 10) for i in range(10)]
print(data)

res = [x for x in data if x >= 0]
print(res)

op = [x * x for x in range(1, 11) if x % 2 == 0]
print(op)

str = [ m + n for m in 'ABC' for n in 'XYZ']
print(str)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
dl = [ k + '=' + v for k, v in d.items()]
print(dl)
# 列表
L = ['Hello', 'World', 'IBM', 'Apple']
Lres = [ s.lower() for s in L]
print(Lres)
# 字典
classStu = { x: randint(60,100) for x in range(1,20)}
stu90 = { k : v  for k,v in classStu.items() if v > 90 }
print(classStu)
print(stu90)
# 集合
s = set(data)
sres =  {x for x in s if x % 3 == 0}
print(sres)

