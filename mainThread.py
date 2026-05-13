a=int(input('Enter a: '))
b=int(input('Enter b: '))
print('Threading')

from threading import Thread

class Hello(Thread):
    def fun(self):
        for i in range(a):
            print("Hello")
class Hi(Thread):
    def fun(self):
        for i in range(b):
            print("Hi")
o = Hello()
o.fun()

i = Hi()
i.fun()
