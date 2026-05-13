a=int(input('Enter a: '))
b=int(input('Enter b: '))
try:
    print(a/b)
except Exception as e:
    print("exception",e)
finally:
    print("bye")
