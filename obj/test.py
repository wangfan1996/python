class MyClass:
    i = 12345
    
    def __init__(self,name="",age=""):
        self.name = name
        self.age = age

    def f(self):
        return "hello world"

    def getName(self):
        return self.name

x = MyClass("王帆",23)
print(x.i)
print(x.f())
print(x.getName())
