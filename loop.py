# for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
print('Index|Value')
print('----- -------')
for i in range(len(thislist)):
  print(i,'   |',thislist[i])

# while loop
thislist = ["apple", "banana", "cherry"]
i=0
while(i<len(thislist)):
    print(i,':',thislist[i])
    i+=1