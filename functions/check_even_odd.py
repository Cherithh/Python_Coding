class check:
    def __init__(self,a):
        self.a = a
    
    def checking(self):
        if self.a % 2 == 0:
            return "Even"
        else:
            return "Odd"
    
obj = check(8)
print(obj.checking())