#  loop practice

factorial = int(input("Enter the number: "))
total = 1
for i in range(1,factorial+1):
    total *= i
    i+=1
    
print(total)
