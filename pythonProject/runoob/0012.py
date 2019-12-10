# 函数


# 定义函数
def print_me(test):
    # 打印任何传入的字符串
    print(test)


# 调用函数
print_me("我要调用用户自定义函数!")
print_me("再次调用同一函数")


# 不定长参数
# 加了星号 * 的参数会以元组(tuple)的形式导入
def print_info(arg1, *var_tuple):
    print(arg1)
    for var in var_tuple:
        print_info(var)


print_info(70, 60, 50)


# 加了两个星号 ** 的参数会以字典的形式导入
def print_info_1(arg1, **var_dict):
    print(arg1)
    print(var_dict)


print_info_1(40, a=50, b=60)

# 匿名函数
print_1 = lambda arg1, arg2: arg1 + arg2

print(print_1(10, 50))



