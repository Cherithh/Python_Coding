nums = [3,4,5,23,45,67]

smallest = nums[0]
second_smallest = nums[0]

for i in nums:
    if i < smallest:
        second_smallest = smallest
        i = smallest
    elif i < second_smallest and i != smallest:
        i = second_smallest

print(second_smallest)