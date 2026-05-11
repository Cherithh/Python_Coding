# Find Sum of Elements

class sums:
    def elements(self):
        data = input("Enter your numbers with spaced in between: ").split()
        result = 0
        for i in data:
            result += int(i)
        print("the sum is",result)
            

sum = sums()
sum.elements()