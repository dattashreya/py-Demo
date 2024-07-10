thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print('Sorted List array:',thislist)

thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print('Sorted List int Arr:',thislist1)

# sort in desc str
thislist2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist2.sort(reverse = True)
print(thislist2)

# sort in desc Array
thislist3 = [100, 50, 65, 82, 23]
thislist3.sort(reverse = True)
print('Sorted List int Arr:',thislist3)

thislist4 = ["banana", "Orange", "Kiwi", "cherry"]
thislist4.sort(key = str.lower)
print(thislist4)

thislist5 = ["banana", "Orange", "Kiwi", "cherry"]
thislist5.sort()
print(thislist5)