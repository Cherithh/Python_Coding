string = "automation"

# for i in string:
#     count = 0
#     for x in string:
#         if x == i:
#             count+=1
#     print(i,count)

hash_map = {}

for ch in string:
    hash_map[ch] = hash_map.get(ch,0) + 1

print(hash_map)