import p20191110_1846


class MyClass:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello")

    def __str__(self):
        return "My name is " + self.name


class MyClass2(MyClass):
    def world(self):
        print("World")


a = MyClass2("AAABBB")
myStr = str(a)
a.hello()  # => Hello
a.world()  # => World
print(a)
print(myStr)
p20191110_1846.MyClassB.funcAStatic()
