#  Find the Armstrong Number
# ex:153 ---> 1**1 + 5**5 + 3**3

num = int(input("Enter the number: "))
original_num = num
power = len(str(num))

total = 0
while num > 0:
    digit = num % 10
    total = total + (digit ** power)
    num = num // 10

if total == original_num:
    print("Its an Armstrong Number")
else:
    print("Its not an Armstrong Number")