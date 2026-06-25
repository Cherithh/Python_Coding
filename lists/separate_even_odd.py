nums = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []

for i in nums:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)


print(f"Even: {even}\n Odd: {odd}")