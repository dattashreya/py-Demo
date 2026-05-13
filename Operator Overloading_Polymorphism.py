class Student:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x + self.y
a=Student(10,20)
b=Student(10,20)
print('add a:',a.add())
print('add b:',b.add())

# add a: 30
# add b: 30
