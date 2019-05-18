class people:
    name = ''
    age = 0
    __weight = 0
    
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    
    def speak(self):
        print("%s说:我%d岁。" %(self.name,self.age))


class student(people):
    grade = ''

    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g

    def speak(self):
        print("%s说:我%d岁了，我在读%s年级"%(self.name,self.age,self.grade))

class speaker():
    topic = ''
    name = ''
    
    def __init__(self,n,t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(speaker,student):
    
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

s = student("王帆",23,75,"大四")
s.speak()

test = sample("王帆",23,75,"大四","Python")
test.speak()



