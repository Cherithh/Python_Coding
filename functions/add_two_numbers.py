#Function to add two numbers
class addition:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def output(self):
        print(f"Sum of {self.a},{self.b} is {self.add()}")

obj = addition(4,5)
obj.output()