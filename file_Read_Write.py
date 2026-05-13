# reading a file named "MyFile"

f = open('MyFile','r')
print(f.read())  # print entire documents
print(f.readline())  # print first line of document

# writing a file named "myfile1"

f = open('myfile1','w')
f.write("my file 1 context")

# using loop data copy

f = open('MyFile','r')
f1 = open('myfile1','w')
for d in f:
    f1.write(d)

# image print

f=open('image.jpg' , 'rb')
f1=open('imageNew.jpg' , 'wb')
for d in f:
    f1.write(d)

