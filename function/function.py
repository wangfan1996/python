

# abs() 函数返回数字的绝对值。
print ("abs(-40) : ", abs(-40))
print ("abs(100.10) : ", abs(100.10))

#setattr(object, name, value)参数object -- 对象。name -- 字符串，对象属性。value -- 属性值。
class A(object):
    name = "runoob"

a = A()
setattr(a,'age',28)
print(a.age)

exec("pip3 -V")
