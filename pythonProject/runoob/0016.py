class People:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s %d" % (self.name, self.age))
        print(self.__weight)


class Student(People):
    grade = ''
    weight = ''

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.weight = w
        self.grade = g

    def speak(self):
        print("%s %d" % (self.name, self.age))
        print(self.weight)
        print(self.grade)

    def __del__(self):
        print('over')


class Speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print(self.name, self.topic)


class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample('wf', 23, 150, 100, 'python')
test.speak()
super(Sample, test).speak()


class Parent:
    def test_a(self):
        print('f')


class Child(Parent):
    def test_a(self):
        print('z')


c = Child()
c.test_a()
super(Child, c).test_a()
