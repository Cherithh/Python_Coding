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
        
    def output(self):
        print(f"The biggest number in those 3 numbers is: {self.finding()}")

obj = finding_max(5,7,9)
obj.output()