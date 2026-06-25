# Find first digit

num = int(input("Enter the digits: "))

while num >= 10:
    num = num // 10

print(num)
