# 循环语句

n = 100
num = 0
counter = 1
while counter <= n:
    num += counter
    counter = counter + 1

print("1 到 %d 之和为: %d" % (n, num))


count = 0
while count < 5:
    info = "小于 5"
    print(count, info)
    count += 1
else:
    info = "大于或等于 5"
    print(count, info)

languages = ["C", "C++", "Perl", "Python", "PHP", "Java"]

for x in languages:
    if x == 'PHP':
        break
    else:
        print(x, end=' ')

print()
# range()函数生成数列 5开始 9前结束 2步长
for i in range(5, 9, 2):
    print(i, end=' ')

print()


