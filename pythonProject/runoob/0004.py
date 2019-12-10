# 字符串

var1 = 'Hello Word'
var2 = 'Runoob'

print(var1[0])
print(var2[1:5])

print(var1[:6] + var2)

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
print(r'\n')
print(R'\n')

if "H" in a:
    print('in')
else:
    print('not in')

print("我叫%s今年%d岁" % ('小米', 10))

a = 'hellO'
# 将字符串的第一个字母变成大写,其他字母变小写
print(a.capitalize())
# 返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用第二个参数去填充。
print(a.center(10, '*'))
# 统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
print(a.count('l'))
# 检测字符串中是否包含子字符串 str,如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
print(a.find('e'))
# isalnum() 方法检测字符串是否由字母和数字组成。
print(a.isalnum())
# isalpha() 方法检测字符串是否只由字母或文字组成。
print(a.isalpha())
# isdigit() 方法检测字符串是否只由数字组成。
print(a.isdigit())
# islower() 方法检测字符串是否由小写字母组成。
print(a.islower())
# isnumeric() 方法检测字符串是否只由数字组成
print(a.isnumeric())
# isspace()方法检测字符串是否只由空白字符组成。
print(a.isspace())
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
s1 = "-"
s2 = " "
seq = ("r", "u", "n", "o", "o", "b")
print(s1.join(seq))
print(s2.join(seq))
# len() 方法返回对象（字符、列表、元组等）长度或项目个数。
print(len(a))
# 原字符串左对齐,并使用空格填充至指定长度的新字符串
# 截掉字符串左边的空格或指定字符。
b = "Runoob example....wow!!!"
print(b.ljust(50, '*'))
# lower()方法转换字符串中所有大写字符为小写
a = "HellO"
print(a.lower())
# lstrip() 方法用于截掉字符串左边的空格或指定字符。
strA = "     this is string example....wow!!!     "
print(strA.lstrip())
strA = "88888888this is string example....wow!!!8888888"
print(strA.lstrip('8'))


