class table:

    def __init__(self,a):
        self.a = a

    def multiply(self):
        for i in range(1,11):
            print(f"{self.a} * {i} = {self.a*i}")

obj = table(9)
obj.multiply()