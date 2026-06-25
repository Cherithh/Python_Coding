nums = [3,5,7,12,45,56]

largest = nums[0]
second_largest = nums[0]

for i in nums:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)