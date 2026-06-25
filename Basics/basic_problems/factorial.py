num = int(input("Enter the number: "))
factorial = 1
if num < 0 :
    print("The number you have typed is less thn 0")
elif num == 0:
    print("There is no factorial for 0")
else:
    for i in range(1,num+1):
        factorial = factorial * i
        
    print(factorial)