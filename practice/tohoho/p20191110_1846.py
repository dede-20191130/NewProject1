class MyClassA:
    def funcA(self):
        print("MyClassA:funcA")


# print
# "MyClassA:funcA"


class MyClassB:

    def funcA(self):
        print("MyClassB:funcB")

    @staticmethod
    def funcAStatic():
        print("MyClassB:funcB")


# print
# "MyClassB:funcB"


class MyClassC(MyClassA, MyClassB):
    pass


a = MyClassC()
a.funcA()  # MyClassA のメソッドもAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# a.funcB()  # MyClassB のメソッドも使用できる
MyClassB.funcAStatic()
