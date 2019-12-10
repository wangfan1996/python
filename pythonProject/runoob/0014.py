# 读写文件

# 打开一个文件
f = open("foo.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# 关闭打开的文件
f.close()

# 打开一个文件
f = open("foo.txt", "r")
strLine = f.readline()
print(strLine)
# 关闭打开的文件
f.close()

# 打开一个文件
f = open("foo.txt", "r")
strLine = f.readlines()
print(strLine)
# 关闭打开的文件
f.close()


# 打开一个文件
f = open("foo.txt", "r")
for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()

