arr = [10,25,7,99,45]

largest = 0
second_largest = 0
for num in arr:
    if num > largest:
        largest = num

for num in arr:
    if num > second_largest and num != largest:
        second_largest = num

print(num)