# 数字Number
import math
import random

var1 = 1
var2 = 10

number = 0xA0F
print(number)
number = 0o37
print(number)

number = 5
print(number ** 2)

# 求绝对值
print(abs(-5))

# 向上取整
print(math.ceil(4.1))

# 返回数字的绝对值
print(math.fabs(-10.0))

# 向下取整
print(math.floor(4.9))

# 返回整数部分和小数部分
print(math.modf(3.1415926))

# 2的3次方
print(math.pow(2, 3))

# 四舍五入
print(round(3.4))

# 平方根
print(math.sqrt(4))

# 从序列的元素中随机挑选出一个元素
print(random.choice(range(100)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))

# 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
print(random.randrange(1, 10, 2))

# 随机生成下一个实数，它在[0,1)范围内。
print(random.random())

# 将序列的所有元素随机排序
listTest = [20, 16, 10, 5]
random.shuffle(listTest)
print("随机排序列表 : ", listTest)

# uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内。
print(random.uniform(0, 10))

print(math.pi)
print(math.e)
