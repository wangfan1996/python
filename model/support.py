def print_func(par):
    print("Hello :",par)

#斐波拉数列
def fib(n):
    a,b=0,1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b
    print()

#返回到n的斐波拉数列
def fib2(n):
    result = []
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result

if __name__  == '__main__':
    print("程序自身在运行")
else:
    print("我来自另一模块")

