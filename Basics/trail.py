# reverse of a number

num = int(input("Enter the number: "))

rev = 0

while num > 0:
    total = num % 10
    rev = (rev * 10) + total
    num = num // 10

print(rev)

