class Computer:
    
    def __init__(self, ram , cpu):
        self.ram = ram
        self.cpu = cpu
    
    def config(self):
        print('Config: ',self.ram , self.cpu)

obj = Computer('8gb','i3')
Computer.config(obj)
