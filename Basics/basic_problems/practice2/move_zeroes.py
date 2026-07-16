nums = [1,2,0,4,0,5,0,6]
result = []
for i in nums:
    if i != 0:
        result.append(i)
len = len(nums) - len(result)

for i in range(1,len+1):
    result.append(0)


print(result)