class C:
    def __init__(self):
        print("C init method constructor")
    def fun1(self):
        print("func 1 works")
    def fun2(self):
        print("func 2 works")
class D(C):
    def __init__(self):
        super().__init__()
        print("D init method constructor")
    def fun3(self):
        print("func 3 works")
    def fun4(self):
        print("func 4 works")
d = D()
d.fun3()
d.fun4()
d.fun1()
d.fun2()
