nums = [20,40,50,38,60]
largest = []
second_largest = []
for num in nums:
    if num > largest:
     largest.append(num)

for i in nums:
    if i > second_largest and i not in largest:
        second_largest.append(i)

print(second_largest)