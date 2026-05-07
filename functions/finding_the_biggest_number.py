class finding_max:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def finding(self):
        if self.a >= self.b and self.a >= self.c:
            return self.a
        elif self.b >= self.a and self.b >= self.c:
            return self.b
        else:
            return self.c
        
obj = finding_max(4,6,8)
print(obj.finding())