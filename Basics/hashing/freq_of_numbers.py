n = [5,3,5,2,4,3,1,2,6,7,8]

# for num in n:
#     count = 0
#     for x in n:
#         if x == num:
#             count+=1
#     print(num,count)


freq = {}

for num in n :
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1
print(freq)