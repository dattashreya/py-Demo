print("hello world")
print(1+23)
name = 'Shreya '
d = name + 'Datta'
print(d)
print(d[0])
print(d[0:3])
print(d[-1])

# list in python is a collection of items which are ordered and changeable. It allows duplicate members.

number = [  1, 2, 3, 4, 5 ]
print(number)
arrNum = [ 1, 2, 3, 4, 5 ]
strNum = [ 'one', 'two', 'three', 'four', 'five' ]
newArr = [ arrNum, strNum ]
print(newArr)
(arrNum.append(6)) # append adds an element to the end of the list
(arrNum.insert(0, 10)) # insert adds an element at the specified index, in this case 0, which is the beginning of the list
print(arrNum)
arrNum.pop(0) # pop removes an element at the specified index, in this case 0, which is the beginning of the list
print(arrNum)
print('length-', len(arrNum)) # len returns the number of elements in the list
print('max number-', max(arrNum)) # max returns the maximum element in the list, in this case it will return the maximum element in arrNum which is 6
print('min number-', min(arrNum)) # min returns the minimum element in the list, in this case it

# tuple in python is a collection of items which are ordered and unchangeable. It allows duplicate members.
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
tuple1[1]=10 # this will give an error because tuples are immutable, meaning they cannot be changed after they are created.
print(tuple1)