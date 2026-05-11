import math
x= math.sqrt(16) # sqrt is a function in the math module that returns the square root of a number.
print(x)

y=pow(2,3)
print(y) # pow is a function in the math module that returns the value of a number raised to the power of another number, in this case 2 raised to the power of 3 which is 8.

# swap with temp
a=9
b=8
temp=a
a=b
b=temp
print(a,' ',b)

# swap without temp
a=9
b=8
a=a+b
b=a-b
a=a-b
print(a,' ',b)

print('calc module  imported successfully')
from Calc import *
print(add(2,3))
print(subtract(2,3))
print(multiply(2,3))
print(divide(2,3))