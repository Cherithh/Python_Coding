# num = 153
# n = num

# power = len(str(num))
# total = 0

# while n > 0:
#     ld = n % 10
#     total = total + (ld ** power)
#     n = n // 10

# if total == num:
#     print("Armstrong")
# else:
#     print("Not Armstrong")



for i in range(100,1000):
    power = len(str(i))
    total = 0
    temp = i
    while temp > 0:
        ld = temp % 10
        total = total + (ld ** power)
        temp = temp // 10
    if total == i:
        print(i)
