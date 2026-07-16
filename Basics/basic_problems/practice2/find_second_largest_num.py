nums = [2,4,6,7,8,5,3,5,9]

largest_num = max(nums)
second_largest_num = []
for i in nums:
    if i != largest_num:
        second_largest_num.append(i)

print(max(second_largest_num))