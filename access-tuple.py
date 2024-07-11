thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[2])
print(thistuple[-1])

print(thistuple[1:])
print(thistuple[:])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
  print("Not present")