nums = [1,0,2,0,3,0,4,0,5,0]
result = []
for i in nums:
    if i != 0:
        result.append(i)

zero_count = len(nums) - len(result)

for i in range(zero_count):
    result.append(0)

print(result)