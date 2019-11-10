class MyClassA:
    def funcA(self):
        print
        "MyClassA:funcA"


class MyClassB:
    def funcB(self):
        print
        "MyClassB:funcB"


class MyClassC(MyClassA, MyClassB):
    pass


a = MyClassC()
a.funcA()  # MyClassA のメソッドもa
a.funcB()  # MyClassB のメソッドも使用できる
