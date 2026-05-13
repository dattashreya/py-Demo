a=int(input('Enter a: '))
b=int(input('Enter b: '))
print('Multi-threading')
class Hello:
    def fun(self):
        for i in range(a):
            print("Hello")
class Hi:
    def fun(self):
        for i in range(b):
            print("Hi")
o = Hello()
o.fun()

i = Hi()
i.fun()

# Enter a: 4
# Enter b: 4
# Multi-threading
# Hello
# Hello
# Hello
# Hello
# Hi
# Hi
# Hi
# Hi
