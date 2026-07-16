
# Remove duplicates
# nums = [1,2,3,4,5,6,5,4,3]
# result = []
# for i in nums:
#     if i not in result and  nums.count(i) == 1:
#         result.append(i)

# print(result)

# Find duplicates
nums = [1,2,3,4,5,4,1,2]
result = []
for i in nums:
    if i not in result and nums.count(i) >=2:
        result.append(i)

print(result)