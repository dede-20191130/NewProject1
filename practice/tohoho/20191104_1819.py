class MyClass:
    def __init__(self):
        self.name = "ishikawa"  # インスタンス変数


a0 = MyClass()

a1 = MyClass()
a1.name = "Tanaka"

a2 = MyClass()
a2.name = "Suzuki"

print(a0.name)
print(a1.name)  # => Tanaka
print(a2.name)  # => Suzuki
