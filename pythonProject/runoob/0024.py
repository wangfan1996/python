# 日期时间
import time
import calendar

ticks = time.time()
print('当前时间戳：%s' % ticks)

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

# 获取格式化的时间
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)


# strftime格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


cal = calendar.month(2019, 12)
print(cal)


scale = 50
print("执行开始".center(scale//2, "-"))  # .center() 控制输出的样式，宽度为 25//2，即 22，汉字居中，两侧填充 -
start = time.perf_counter()     # 返回系统运行时间
for i in range(scale+1):    # 0-50
    a = '*' * i             # i 个长度的 * 符号
    b = '.' * (scale-i)  # scale-i个长度的 . 符号。符号 * 和 . 总长度为50
    c = (i/scale)*100  # 显示当前进度，百分之多少
    dur = time.perf_counter() - start    # 计时，计算进度条走到某一百分比的用时
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    # \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；{:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；{}，对应输出的数为a；{}，对应输出的数为b；{:.2f}，输出有两位小数的浮点数，对应输出的数为dur；end=''，用来保证不换行，不加这句默认换行。
    time.sleep(0.2)     # 在输出下一个百分之几的进度前，停止0.1秒
print("\n"+"执行结果".center(scale//2, '-'))

