class Computer:
    def __init__(self):
        self.name = "Shreya"
        self.age = "20"
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = Computer()
c2 = Computer()
print(c1.name , ',',c1.age)
print(c2.name , ',',c2.age)
if c1.compare(c2):
    print("They are the same")
else:
    print("They are different")
