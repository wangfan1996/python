# 条件控制

# 斐波拉数列
a, b = 0, 1
while b < 10:
    print(b, end=' ')
    a, b = b, a+b
print()

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)

print("Good bye!")

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

# 退出提示
input("点击 enter 键退出")

number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")


num = int(input("请输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("可以整除 2 和 3")
    else:
        print("可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("可以整除 3，但不能整除 2")
    else:
        print("不能整除 2 和 3")



