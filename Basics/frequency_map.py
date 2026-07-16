nums = [1,2,3,4,5,4,3,2,7,8,99,6,7,8]

freq = dict()

for i in range(1,len(nums)):
    if nums[i] in freq:
        freq[nums[i]] += 1
    else:
         freq[nums[i]] = 1

print(freq)