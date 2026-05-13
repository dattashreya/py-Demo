class Student:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x + self.y
a=Student(10,20)
b=Student(20,20)
s=a.add()
s1=b.add()
print('add a:',s)
print('add b:',s1)

if(s==s1):
    print(f"{s} is same {s1}")
if(s>s1):
    print(f"{s} is greater {s1}")
else:
    print(f"{s} is lesser {s1}")
