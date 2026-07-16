n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

freq = dict()
for num in n:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1

for num in m:
    print(freq.get(num,0)) 










# hash_list = [0] * 11

# for num in n:
#     hash_list[num]+=1
# for num in m:
#     if num < 1 or num > 10:
#         print(0)
#     else:
#         print(hash_list[num])