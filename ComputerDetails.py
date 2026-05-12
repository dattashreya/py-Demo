class Computer:
    sch = "SGHS"
    def __init__(self):
        self.name = "SD"
        self.age = 10
    def details(self):
        return (self.name, self.age)
c = Computer()
c1 = Computer()
print(c.details())
print(c1.details())
