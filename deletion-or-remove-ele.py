# remove items from list
thislist = [
    "apple", "banana", "cherry",
    "lemon","watermelon"]
print(thislist)

thislist.remove("lemon")
print(thislist)

# remove last element
thislist.pop()
print(thislist)

# delete
del thislist[0]
print(thislist)

# clear the total list but the array will remain empty existence
thislist.clear()
print(thislist)

# delete the array total itself
del thislist
print(thislist)
# throws error as for no existence