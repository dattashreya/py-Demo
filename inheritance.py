class C:
    def fun1(self):
        print("func 1 works")
    def fun2(self):
        print("func 2 works")
class D(C):
    def fun3(self):
        print("func 3 works")
    def fun4(self):
        print("func 4 works")
obj = C()
obj.fun1()
obj.fun2()

d = D()
d.fun3()
d.fun4()
d.fun1()
