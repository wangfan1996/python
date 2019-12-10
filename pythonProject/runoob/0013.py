import sys
from support import print_func
import support

for i in sys.argv:
    print(i)

print(sys.argv)
print(sys.argv[0])

print_func(1)
support.print_func(1)

# dir()可以找到模块内定义的所有名称
print(dir())

