# sum of even numbers

num = input("Enter the number: ").replace(" ","")
count = 0

for i in num:
    if int(i) % 2 != 0:
        count += 1

print(count)