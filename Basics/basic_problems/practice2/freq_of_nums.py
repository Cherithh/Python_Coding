nums = [1,2,3,4,5,4,3,6,7,8]
# visited= []
# for n in nums:
#   if n not in visited:
#     count = 0
#     for x in nums:
#         if x == n:
#             count+=1
#     print(n,count)
#     visited.append(n)

freq = {}

for n in nums:
    if n in freq:
        freq[n]+=1
    else:
        freq[n]=1

for key, value in freq.items():
    print(key,value)