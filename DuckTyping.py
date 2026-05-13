class PyCharm:
    def execute(self):
        print("running...")
class Eclipse:
    def execute(self):
        print("authenticating...")
        print("running...")
class Laptop:
    def code(self,ide):
        ide.execute()
        
ide = Eclipse()

l = Laptop()
l.code(ide)

# authenticating...
# running...
