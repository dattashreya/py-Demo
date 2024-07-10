mylist = ["apple","apple", "banana", "cherry"]
print(type(mylist))
print(mylist)
# duplicate entry is possible in list
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

thislist = ["apple", "banana", "cherry","banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[1:5])
print(thislist[:4])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
