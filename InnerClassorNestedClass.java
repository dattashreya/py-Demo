# nested class or inner class
class Computer:
    def __init__(self):
            self.name = "Shreya"
            self.age = "16"
            self.laptop = self.Laptop()
    class Laptop:
        def __init__(self):
            self.name = "Asus"
            self.ram = "16gb"
c1 = Computer()
print(c1.name , ',',c1.age)
print(c1.laptop.name , ',',c1.laptop.ram)
